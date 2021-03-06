# Generated by Django 3.2 on 2022-01-02 15:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0006_alter_usertable_tabs_switch'),
    ]

    operations = [
        migrations.AlterField(
            model_name='response_table',
            name='answer',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='response_table',
            name='question',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='exam.question'),
        ),
        migrations.AlterField(
            model_name='response_table',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='exam.usertable'),
        ),
    ]
