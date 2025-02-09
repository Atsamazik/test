from rest_framework import serializers, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth.models import User
from django.conf import settings
from .models import (
    Form, Question, Answer, FormConnector, UserRequest,
    RequestWithAnswer, RequestWithText, RequestWithBoolean,
    RequestWithFile, RequestWithNumber
)


# Основные сериализаторы
class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class FormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Form
        fields = '__all__'


# Сериализаторы для разных типов ответов
class RequestWithAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestWithAnswer
        fields = '__all__'


class RequestWithTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestWithText
        fields = '__all__'


class RequestWithBooleanSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestWithBoolean
        fields = '__all__'


class RequestWithFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestWithFile
        fields = '__all__'


class RequestWithNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestWithNumber
        fields = '__all__'

