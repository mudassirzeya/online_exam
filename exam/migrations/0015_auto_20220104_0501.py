# Generated by Django 3.2 on 2022-01-03 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0014_auto_20220104_0458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setting_table',
            name='exam_end_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='setting_table',
            name='exam_start_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
