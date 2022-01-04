from django.urls import path
from .views import student_loginpage, student_home, tabs_switch, question_upload, logout_user, clear_answer, student_register, add_new_users, admin_page, add_setting, setting_page, user_data_page

urlpatterns = [
    path('student_login/', student_loginpage, name='student_login'),
    path('', student_home, name='student_home'),
    path('tabs_switch/', tabs_switch, name='tabs_switch'),
    path('upload_question/', question_upload, name='upload_question'),
    path('logout_user/', logout_user, name='logout_user'),
    path('clear_answer/', clear_answer, name='clear_answer'),
    path('student_register/', student_register, name='student_register'),
    path('add_new_user/', add_new_users, name='add_new_user'),
    path('admin_page/', admin_page, name='admin_page'),
    path('add_setting/', add_setting, name='add_setting'),
    path('setting_page', setting_page, name='setting_page'),
    path('all_user_page', user_data_page, name='all_user_page'),

]
