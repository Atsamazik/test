# Generated by Django 5.1.6 on 2025-02-09 17:24

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0002_requestwithnumber_form_is_start_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='answer',
            options={'verbose_name': 'ответ', 'verbose_name_plural': 'Ответы'},
        ),
        migrations.AlterModelOptions(
            name='form',
            options={'verbose_name': 'форму', 'verbose_name_plural': 'Формы'},
        ),
        migrations.AlterModelOptions(
            name='formconnector',
            options={'verbose_name': 'связь форм', 'verbose_name_plural': 'Связи форм по вопросу'},
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'verbose_name': 'вопрос', 'verbose_name_plural': 'Вопросы'},
        ),
        migrations.AlterField(
            model_name='answer',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Последнее изменение'),
        ),
        migrations.AlterField(
            model_name='form',
            name='is_start',
            field=models.BooleanField(default=False, verbose_name='Является начальной формой'),
        ),
        migrations.AlterField(
            model_name='form',
            name='note',
            field=models.TextField(verbose_name='Комментарий'),
        ),
        migrations.AlterField(
            model_name='form',
            name='title',
            field=models.TextField(verbose_name='Название формы'),
        ),
        migrations.AlterField(
            model_name='form',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Последнее изменение'),
        ),
        migrations.AlterField(
            model_name='question',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Последнее изменение'),
        ),
        migrations.AlterField(
            model_name='userrequest',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
