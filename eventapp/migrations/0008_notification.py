# Generated by Django 4.2.6 on 2023-12-14 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventapp', '0007_remove_teacher_staff_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('description', models.CharField()),
            ],
        ),
    ]