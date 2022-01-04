from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Section (models.Model):
    section = models.CharField(max_length=100, null=True)

    def __str__(self) -> str:
        return self.section


class Question (models.Model):
    section_dropdown = models.ForeignKey(
        Section, null=True, on_delete=models.CASCADE)
    question_text = models.TextField(null=True, blank=True)
    question_image = models.TextField(null=True, blank=True)
    option_a = models.TextField(null=True, blank=True)
    option_a_image = models.TextField(null=True, blank=True)
    option_b = models.TextField(null=True, blank=True)
    option_b_image = models.TextField(null=True, blank=True)
    option_c = models.TextField(null=True, blank=True)
    option_c_image = models.TextField(null=True, blank=True)
    option_d = models.TextField(null=True, blank=True)
    option_d_image = models.TextField(null=True, blank=True)
    marks = models.IntegerField(null=True, blank=True)

    def __str__(self) -> str:
        return str(self.section_dropdown) + '-' + str(self.id)


class UserTable (models.Model):
    USERTYPE = (
        ('student', 'student'),
        ('staff', 'staff'),
    )
    user = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    registration = models.CharField(max_length=100, null=True, blank=True)
    tabs_switch = models.PositiveBigIntegerField(null=True, default=0)
    user_type = models.CharField(
        max_length=100, null=True, blank=True, choices=USERTYPE)

    def __str__(self) -> str:
        return str(self.name) + '-' + str(self.registration)


class Response_Table (models.Model):
    user = models.ForeignKey(UserTable, null=True,
                             blank=True, on_delete=models.CASCADE)
    question = models.ForeignKey(
        Question, null=True, blank=True, on_delete=models.CASCADE)
    answer = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self) -> str:
        return str(self.user)


class Setting_Table (models.Model):
    ALLOW = (
        ('YES', 'YES'),
        ('NO', 'NO'),
    )
    msg_when_not_started = models.TextField(null=True, blank=True)
    instruction_for_exam = models.TextField(null=True, blank=True)
    inst_when_time_out_during_exam = models.TextField(null=True, blank=True)
    Instruction_when_Logging_in_after_time_out = models.TextField(
        null=True, blank=True)
    msg_when_submit = models.TextField(null=True, blank=True)
    exam_start_time = models.DateTimeField(
        auto_now_add=False, blank=True, null=True)
    exam_end_time = models.DateTimeField(
        auto_now_add=False, blank=True, null=True)
    math_and_bio = models.TextField(null=True, blank=True)
    allow_registration = models.CharField(
        max_length=10, null=True, blank=True, choices=ALLOW)
    add_student_link = models.CharField(max_length=500, null=True, blank=True)
    add_question_link = models.CharField(
        max_length=500, null=True, blank=True)
