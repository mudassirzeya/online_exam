# Generated by Django 3.2 on 2022-01-03 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0011_auto_20220104_0105'),
    ]

    operations = [
        migrations.AddField(
            model_name='setting_table',
            name='allow_registration',
            field=models.CharField(blank=True, choices=[('YES', 'YES'), ('NO', 'NO')], max_length=10, null=True),
        ),
    ]