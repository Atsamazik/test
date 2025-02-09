import nested_admin
from django.contrib import admin
from .models import Form, Question, Answer, FormConnector


class AnswerInline(nested_admin.NestedTabularInline):
    model = Answer
    extra = 1  # Количество пустых строк для добавления
    fields = ('body',)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "question":
            # Ограничиваем выбор вопросов только теми, которые имеют тип MUL_O или ONE_O
            kwargs["queryset"] = Question.objects.filter(question_type__in=['MUL_O', 'ONE_O'])
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class QuestionInline(nested_admin.NestedStackedInline):
    model = Question
    extra = 1  # Количество пустых строк для добавления
    fields = ('body', 'note', 'required', 'question_type')
    inlines = [AnswerInline]  # Вложенные ответы


@admin.register(Form)
class FormAdmin(nested_admin.NestedModelAdmin):
    list_display = ('title', 'is_start', 'updated_at')
    inlines = [QuestionInline]  # Вложенные вопросы


@admin.register(FormConnector)
class FormConnectorAdmin(admin.ModelAdmin):
    pass
