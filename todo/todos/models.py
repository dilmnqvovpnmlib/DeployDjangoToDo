from django.contrib.auth.models import User
from django.db import models

from todo.models import ModelBase


class Tag(ModelBase):
    class Meta:
        verbose_name = verbose_name_plural = 'Tag'
        ordering = ['order']

    order = models.IntegerField("表示順")
    name = models.CharField("名称", max_length=256)

    def __str__(self):
        return self.name


class Todo(ModelBase):
    class Meta:
        verbose_name = verbose_name_plural = 'Todo'
        ordering = ['-created']
    content = models.CharField("内容", max_length=256)
    completed = models.DateTimeField("完了日時", blank=True, null=True)
    user = models.ForeignKey(User, verbose_name="登録者", on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, verbose_name="Tags")

    def __str__(self):
        return self.content
