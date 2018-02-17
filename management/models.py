from django.db import models
from django.utils import timezone


class Charge(models.Model):
    name = models.CharField('サイトの名前', max_length=20)
    num = models.IntegerField('件数')
    charge = models.IntegerField('件数分の合計金額')
    created_at = models.DateTimeField('日付', default=timezone.now)

    def __str__(self):
        return self.name


