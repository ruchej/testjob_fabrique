from django.db import models


class Poll(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название")
    start_date = models.DateField(editable=False, verbose_name="Дата начала")
    end_date = models.DateField(editable=True, verbose_name="Дата окончания")
    description = models.TextField(blank=True, verbose_name="Описание опроса")
    quesions = models.ManyToManyField('Question', blank=True, verbose_name='Вопросы')

    class Meta:
        verbose_name = "Опрос"
        verbose_name_plural = "Опросы"

    def __str__(self):
        return self.title


class Question(models.Model):
    QUESTION_TYPE = (
            (1, "Выбор одного варианта"),
            (2, "Выбор нескольких вариантов"),
            (3, "Ответ текстом"),
        )
    content = models.TextField(max_length=2000, unique=True, verbose_name="Текст вопроса")
    question_type = models.CharField(
        max_length=1, choices=QUESTION_TYPE, default=1, verbose_name="Тип вопроса"
    )

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"

    def __str__(self):
        return f'{self.id}. {self.content}'


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='Вопрос')
    content = models.TextField(verbose_name="Содержание ответа")

    class Meta:
        verbose_name = "Ответ"
        verbose_name_plural = "Ответы"

    def __str__(self):
        return f'{self.id}. {self.content}'
