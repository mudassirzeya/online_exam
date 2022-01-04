from django.contrib import admin
from .models import UserTable, Question, Response_Table, Section, Setting_Table

# Register your models here.

admin.site.register(Section)
admin.site.register(Question)
admin.site.register(UserTable)
admin.site.register(Response_Table)
admin.site.register(Setting_Table)
