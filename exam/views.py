from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Setting_Table, Question, Response_Table, UserTable, Section
from django.contrib.auth.decorators import login_required
from datetime import datetime
from urllib.request import urlopen
from .forms import SettingForm
import pytz
import json
import time


# Create your views here.


def student_loginpage(request):
    setting = Setting_Table.objects.all().first()
    UTC = pytz.utc
    if request.method == 'POST':
        data = json.loads(request.body)
        user_data = data['data_obj'][0]
        print("login: ", user_data)
        username = user_data['email']
        password = user_data['password']
        user = authenticate(request, username=username, password=password)
        setting_table = Setting_Table.objects.all().first()
        exam_start_time = setting_table.exam_start_time
        exam_end_time = setting_table.exam_end_time
        msg_when_not_started = setting_table.msg_when_not_started
        Instruction_when_Logging_in_after_time_out = setting_table.Instruction_when_Logging_in_after_time_out
        print("time: ", exam_start_time)
        current_time = datetime.now(UTC)
        print("gmt: ", current_time)
        if user is not None:
            if exam_start_time > current_time:
                # print("exam not started")
                return JsonResponse({'msg': 'not_started', 'error_msg': msg_when_not_started})
                # return redirect('student_login')
            elif exam_end_time < current_time:
                print('exam over')
                return JsonResponse({'msg': 'over', 'error_msg': Instruction_when_Logging_in_after_time_out})
                # return redirect('student_login')
            else:
                login(request, user)
                usertype = UserTable.objects.get(user=request.user)
                if usertype.user_type == 'student':
                    # print("entered exam hall")
                    return redirect('student_home')
                else:
                    return redirect('admin_page')
        else:
            return JsonResponse({'msg': 'wrong'})
            # return render(request, 'student_login.html')
    else:
        print(request.user)
        context = {'setting': setting}
        return render(request, 'student_login.html', context)


def student_register(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_data = data['data_obj'][0]
        print(user_data)
        try:
            existing_user = User.objects.get(username=user_data['email'])
        except:
            existing_user = None
        if existing_user is not None:
            return JsonResponse({'msg': 'already'})
        else:
            new_user = User.objects.create_user(
                username=user_data['email'], password='12345')
            new_user.email = user_data['email']
            new_user.save()
            UserTable.objects.create(
                user=new_user,
                name=user_data['name'],
                email=user_data['email'],
                user_type='student',
            )
            return JsonResponse({'msg': 'success'})
    return render(request, 'student_login.html')


def add_new_users(request):
    if request.method == 'POST':
        input = request.POST.get('confirm')
        if input == 'confirm':
            all_users = UserTable.objects.filter(user_type='student')
            for user_item in all_users:
                user = User.objects.get(id=user_item.user.id)
                user.delete()
                print('user: ', user)
            add_user_url = Setting_Table.objects.filter().first()
            url = add_user_url.add_student_link
            response = urlopen(url)
            data_json = json.loads(response.read())
            for data in data_json:
                new_user = User.objects.create_user(
                    username=data['Email'], password=str(data['Registration']))
                new_user.email = data['Email']
                new_user.save()
                UserTable.objects.create(
                    user=new_user,
                    name=data['Name'],
                    email=data['Email'],
                    registration=data['Registration'],
                    user_type='student',
                )
            return redirect('setting_page')
        else:
            messages.info(request, 'You Entered Wrong Input')
    context = {}
    return render(request, 'admin_page.html', context)


@login_required(login_url='student_login')
def student_home(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_answers_data = data['data_obj']
        question_id = int(user_answers_data[0]['question'])
        question = Question.objects.get(id=question_id)
        user_data = UserTable.objects.get(user=request.user)
        user_response_data = Response_Table.objects.filter(
            user=user_data, question=question)
        if user_response_data:
            user_response_data.delete()
            Response_Table.objects.create(
                user=user_data,
                question=question,
                answer=user_answers_data[0]['user_answer'],
            )
        else:
            Response_Table.objects.create(
                user=user_data,
                question=question,
                answer=user_answers_data[0]['user_answer'],
            )
        print("data: ", user_answers_data)
        time.sleep(1)
        return JsonResponse({'msg': 'success'})
    questions = Question.objects.all()
    questions_count = questions.count()
    section = Section.objects.all()
    print('section: ', section)
    user_data = UserTable.objects.get(user=request.user)
    user_response_data = Response_Table.objects.filter(user=user_data)
    # qs_json = serializers.serialize('json', user_response_data)
    print("array", user_data.name)
    user_atempt = []
    for subject in section:
        this_sec_question = []
        questions = Question.objects.filter(section_dropdown=subject)
        if len(questions) > 0:
            for each_qs in questions:
                user_response = user_response_data.filter(question=each_qs)
                answer = 'no'
                if user_response:
                    answer = user_response[0].answer
                temp = {"question": each_qs, "answer": answer}
                this_sec_question.append(temp)
        user_atempt.append([subject, this_sec_question])
        # print(questions)
    # print(user_atempt)
    setting_data = Setting_Table.objects.all().first()
    exam_end_time = setting_data.exam_end_time
    millisec = exam_end_time.timestamp() * 1000
    print(millisec)
    context = {'questions': questions,
               'section': section,
               'user_data': user_data,
               'user_response_data': user_response_data,
               'setting_data': setting_data,
               'questions_count': questions_count,
               'user_atempt': user_atempt,
               'millisec': millisec,
               }
    return render(request, 'home.html', context)


@login_required(login_url='student_login')
def tabs_switch(request):
    if request.method == 'POST':
        # data = json.loads(request.body)
        user_data = UserTable.objects.get(user=request.user)
        user_data.tabs_switch += 1
        user_data.save()
        # add_tab_switch = int(tab_switch) + 1
        print('tab', user_data)
        return JsonResponse({'msg': 'success'})
    return render(request, 'home.html')


@login_required(login_url='student_login')
def question_upload(request):
    if request.method == 'POST':
        input = request.POST.get('confirm')
        if input == 'confirm':
            add_user_url = Setting_Table.objects.filter().first()
            url = add_user_url.add_question_link
            response = urlopen(url)
            data_json = json.loads(response.read())
            all_question = Question.objects.all()
            if all_question:
                all_question.delete()
            all_section = Section.objects.all()
            if all_section:
                all_section.delete()
            for data in data_json:
                sections_data = data[0]
                add_section = Section.objects.create(section=sections_data)
                section_query = Section.objects.get(id=add_section.id)
                all_section_question = data[1]
                for questions_data in all_section_question:
                    Question.objects.create(
                        section_dropdown=section_query,
                        question_text=questions_data['Question_Text'],
                        question_image=questions_data['Question_image'],
                        option_a=questions_data['A'],
                        option_a_image=questions_data['A_image'],
                        option_b=questions_data['B'],
                        option_b_image=questions_data['B_image'],
                        option_c=questions_data['C'],
                        option_c_image=questions_data['C_image'],
                        option_d=questions_data['D'],
                        option_d_image=questions_data['D_image'],
                        marks=questions_data['Marks'],
                    )
            return redirect('setting_page')
        else:
            messages.info(request, 'You Entered Wrong Input')
    return render(request, 'admin_page.html')


@login_required(login_url='student_login')
def clear_answer(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        question_id = data['data_obj']
        question = Question.objects.get(id=question_id)
        user_data = UserTable.objects.get(user=request.user)
        user_response_data = Response_Table.objects.filter(
            user=user_data, question=question)
        if user_response_data:
            user_response_data.delete()
            time.sleep(1)
            return JsonResponse({'msg': 'success'})
    return render(request, 'home.html')


def logout_user(request):
    if request.method == 'POST':
        logout(request)
        time.sleep(2)
        return JsonResponse({'msg': 'success'})
    return render(request, 'student_login.html')


@login_required(login_url='student_login')
def admin_page(request):
    context = {}
    return render(request, 'admin_page.html', context)


@login_required(login_url='student_login')
def setting_page(request):
    setting_data = Setting_Table.objects.all().first()
    form = SettingForm(instance=setting_data)
    context = {'form': form}
    return render(request, 'setting.html', context)


@login_required(login_url='student_login')
def user_data_page(request):
    questions = Question.objects.all()
    user_data = UserTable.objects.all()
    user_response_data = Response_Table.objects.all()
    final_data = []
    temp_question = ['question']
    temp_section = ['section']
    temp_question_image = ['question_image']
    for each_question in questions:
        question_text = each_question.question_text
        question_image = each_question.question_image
        question_section = each_question.section_dropdown
        temp_question.append(question_text)
        temp_section.append(
            (question_section))
        temp_question_image.append(question_image)
    final_data.append(temp_section)
    final_data.append(temp_question)
    final_data.append(temp_question_image)
    for each_user in user_data:
        temp = [each_user.name]
        for qst in questions:
            final = ""
            user_response = user_response_data.filter(
                user=each_user, question=qst)
            if user_response:
                # print('user', user_response[0].answer)
                final = user_response[0].answer
            temp.append(final)
        final_data.append(temp)
    context = {"final_data": final_data}
    return render(request, 'user_data.html', context)


def add_setting(request):
    form = SettingForm()
    existing_setting = Setting_Table.objects.all()
    if existing_setting:
        existing_setting.delete()
    if request.method == 'POST':
        form = SettingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('setting_page')
    context = {'form': form}
    return render(request, 'setting.html', context)
