# Generated by Django 3.2 on 2022-01-03 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0010_setting_table_math_and_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertable',
            name='email',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='usertable',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='usertable',
            name='registration',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
