from django.conf import settings
from django.db import models
from django.urls import reverse


class NotAnsweredManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(answered=False)


class Ticket(models.Model):
    title = models.CharField(max_length=100)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.PROTECT,
                             related_name='tickets')
    description = models.TextField()
    answered = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = models.Manager()
    not_answered = NotAnsweredManager()

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f'Ticket № {self.pk} by {self.user.username}'

    def get_absolute_url(self):
        return reverse('tickets:detail', args=[self.pk])
