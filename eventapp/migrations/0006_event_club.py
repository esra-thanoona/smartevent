# Generated by Django 4.2.6 on 2023-12-12 19:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eventapp', '0005_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='club',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='eventapp.club'),
            preserve_default=False,
        ),
    ]
