# Generated by Django 2.2.1 on 2019-06-11 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_course_trainer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_duration',
            field=models.SmallIntegerField(),
        ),
    ]
