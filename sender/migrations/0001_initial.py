# Generated by Django 4.2.3 on 2023-07-09 12:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContentEmail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headliner', models.CharField(max_length=150, verbose_name='тема письма')),
                ('text', models.TextField(verbose_name='текст письма')),
            ],
        ),
        migrations.CreateModel(
            name='EmailLogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_last_sent', models.DateTimeField(verbose_name='дата последней рассылки')),
                ('status_issue', models.BooleanField(default=False, verbose_name='статус попытки')),
                ('server_respond', models.CharField(blank=True, max_length=50, null=True, verbose_name='ответ сервера')),
            ],
        ),
        migrations.CreateModel(
            name='SendSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('send_time', models.TimeField(verbose_name='Время отправки')),
                ('period', models.IntegerField(default=6, verbose_name='Период')),
                ('status', models.CharField(choices=[('1', 'Created'), ('2', 'In Progress'), ('3', 'Closed')], default='Created', max_length=20, verbose_name='Статус')),
            ],
            options={
                'verbose_name': 'настройка',
                'verbose_name_plural': 'настройки',
            },
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=150, verbose_name='e-mail')),
                ('full_name', models.CharField(blank=True, max_length=150, null=True, verbose_name='фио')),
                ('comment', models.TextField(blank=True, max_length=300, null=True, verbose_name='комментарий')),
                ('customer_content', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sender.contentemail', verbose_name='настройки рассылки')),
                ('customer_send_settings', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sender.sendsettings', verbose_name='настройки рассылки')),
            ],
            options={
                'verbose_name': 'получатель',
                'verbose_name_plural': 'получатели',
            },
        ),
    ]