# Generated by Django 3.2 on 2022-01-03 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0009_alter_usertable_tabs_switch'),
    ]

    operations = [
        migrations.AddField(
            model_name='setting_table',
            name='math_and_bio',
            field=models.TextField(blank=True, null=True),
        ),
    ]
