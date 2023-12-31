# Generated by Django 4.2.3 on 2023-09-03 18:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sender', '0006_alter_sendsettings_send_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='contentemail',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Добавлено'),
        ),
        migrations.AddField(
            model_name='customer',
            name='is_blocked',
            field=models.BooleanField(default=False, verbose_name='заблокирован'),
        ),
        migrations.AddField(
            model_name='sendsettings',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Добавлено'),
        ),
        migrations.AlterField(
            model_name='sendsettings',
            name='send_time',
            field=models.TimeField(verbose_name='Время отправки'),
        ),
    ]
