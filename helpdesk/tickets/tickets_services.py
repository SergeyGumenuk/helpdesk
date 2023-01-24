from django.db import models


class NotAnsweredManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(answered=False)
