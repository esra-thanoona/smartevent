# Generated by Django 4.2.6 on 2023-12-07 18:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eventapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('club_name', models.CharField(max_length=50)),
                ('image', models.FileField(upload_to='images/')),
                ('staff_incharge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eventapp.teacher')),
            ],
        ),
    ]