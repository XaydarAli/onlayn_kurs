# Generated by Django 5.0.7 on 2024-07-20 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0007_alter_course_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speciality',
            name='created',
            field=models.DateTimeField(),
        ),
    ]