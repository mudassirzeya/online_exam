# Generated by Django 3.2 on 2022-01-03 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0013_usertable_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setting_table',
            name='exam_end_time',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='setting_table',
            name='exam_start_time',
            field=models.DateTimeField(blank=True),
        ),
    ]
