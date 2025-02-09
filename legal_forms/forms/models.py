from django.conf import settings
from django.contrib.auth.models import User
from django.db import models


class Form(models.Model):
    title = models.TextField(verbose_name='Название формы')
    note = models.TextField(verbose_name='Комментарий')
    is_start = models.BooleanField(default=False, verbose_name='Является начальной формой')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Последнее изменение')

    def __str__(self):
        return f"Форма '{self.title}'"

    class Meta:
        verbose_name = 'форму'
        verbose_name_plural = 'Формы'


class Question(models.Model):
    body = models.TextField()
    note = models.TextField()
    required = models.BooleanField(default=True)
    question_type = models.CharField(max_length=5, choices=settings.QUESTION_TYPES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Последнее изменение')

    form = models.ForeignKey(Form, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"Вопрос: '{self.body}'"

    class Meta:
        verbose_name = 'вопрос'
        verbose_name_plural = 'Вопросы'


class Answer(models.Model):
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Последнее изменение')

    question = models.ForeignKey(Question, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"Ответ: '{self.body}'"

    class Meta:
        verbose_name = 'ответ'
        verbose_name_plural = 'Ответы'


class FormConnector(models.Model):
    form_from = models.ForeignKey(Form, on_delete=models.DO_NOTHING, related_name='relations_from')
    form_to = models.ForeignKey(Form, on_delete=models.DO_NOTHING, related_name='relations_to')
    question_condition = models.ForeignKey(Question, on_delete=models.DO_NOTHING)
    leh_condition = models.CharField(max_length=1, choices={">": "higher", "=": "equal", "<": "lower"})
    answer_condition = models.ForeignKey(Answer, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"Переход из '{self.form_from}' к '{self.form_to}'"

    class Meta:
        verbose_name = 'связь форм'
        verbose_name_plural = 'Связи форм по вопросу'


class UserRequest(models.Model):
    form = models.ForeignKey(Form, on_delete=models.DO_NOTHING)
    question = models.ForeignKey(Question, on_delete=models.DO_NOTHING)


class RequestWithAnswer(UserRequest):
    answer = models.ForeignKey(Answer, on_delete=models.DO_NOTHING)


class RequestWithText(UserRequest):
    text = models.TextField()


class RequestWithBoolean(UserRequest):
    yes_or_no = models.BooleanField()


class RequestWithFile(UserRequest):
    file_url = models.CharField(max_length=255)


class RequestWithNumber(UserRequest):
    number = models.FloatField()
