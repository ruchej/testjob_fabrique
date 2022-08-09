from django.contrib import admin
from .models import Poll, Question, Answer


class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 3
    fields = ('content',)


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_type', 'content')
    inlines = (AnswerInline,)


@admin.register(Poll)
class PollAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'end_date')
