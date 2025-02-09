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
from .serializers import *

from rest_framework.permissions import AllowAny


class RequestWithAnswerViewSet(viewsets.ModelViewSet):
    queryset = RequestWithAnswer.objects.all()
    serializer_class = RequestWithAnswerSerializer


class RequestWithTextViewSet(viewsets.ModelViewSet):
    queryset = RequestWithText.objects.all()
    serializer_class = RequestWithTextSerializer


class RequestWithBooleanViewSet(viewsets.ModelViewSet):
    queryset = RequestWithBoolean.objects.all()
    serializer_class = RequestWithBooleanSerializer


class RequestWithFileViewSet(viewsets.ModelViewSet):
    queryset = RequestWithFile.objects.all()
    serializer_class = RequestWithFileSerializer


class RequestWithNumberViewSet(viewsets.ModelViewSet):
    queryset = RequestWithNumber.objects.all()
    serializer_class = RequestWithNumberSerializer


from rest_framework import serializers, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from django.conf import settings
from .models import (
    Form, Question, Answer, FormConnector,
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


# Вьюсеты для обработки запросов
class RequestWithAnswerViewSet(viewsets.ModelViewSet):
    queryset = RequestWithAnswer.objects.all()
    serializer_class = RequestWithAnswerSerializer


class RequestWithTextViewSet(viewsets.ModelViewSet):
    queryset = RequestWithText.objects.all()
    serializer_class = RequestWithTextSerializer


class RequestWithBooleanViewSet(viewsets.ModelViewSet):
    queryset = RequestWithBoolean.objects.all()
    serializer_class = RequestWithBooleanSerializer


class RequestWithFileViewSet(viewsets.ModelViewSet):
    queryset = RequestWithFile.objects.all()
    serializer_class = RequestWithFileSerializer


class RequestWithNumberViewSet(viewsets.ModelViewSet):
    queryset = RequestWithNumber.objects.all()
    serializer_class = RequestWithNumberSerializer


class FormSubmissionViewSet(viewsets.ViewSet):
    @action(detail=False, methods=['post'])
    def submit_form(self, request):
        form_data = request.data
        form_id = form_data.get('form_id')

        for question_data in form_data.get('questions', []):
            question_id = question_data.get('question_id')
            answer = question_data.get('answer')

            if isinstance(answer, str):
                RequestWithText.objects.create(form_id=form_id, question_id=question_id, text=answer)
            elif isinstance(answer, bool):
                RequestWithBoolean.objects.create(form_id=form_id, question_id=question_id, yes_or_no=answer)
            elif isinstance(answer, (int, float)):
                RequestWithNumber.objects.create(form_id=form_id, question_id=question_id, number=answer)
            elif isinstance(answer, dict) and 'file_url' in answer:
                RequestWithFile.objects.create(form_id=form_id, question_id=question_id, file_url=answer['file_url'])
            elif isinstance(answer, int):
                RequestWithAnswer.objects.create(form_id=form_id, question_id=question_id, answer_id=answer)

        return Response({'status': 'success'})

