# Generated by Django 4.2.3 on 2023-07-10 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sender', '0005_alter_sendsettings_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sendsettings',
            name='send_time',
            field=models.TimeField(choices=[('00:00', '00:00'), ('08:00', '08:00'), ('10:00', '10:00'), ('12:00', '12:00'), ('14:00', '14:00'), ('16:00', '16:00')], verbose_name='Время отправки'),
        ),
    ]
