# Generated by Django 3.2 on 2022-01-02 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0005_auto_20220102_1718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertable',
            name='tabs_switch',
            field=models.CharField(default=0, max_length=100, null=True),
        ),
    ]
