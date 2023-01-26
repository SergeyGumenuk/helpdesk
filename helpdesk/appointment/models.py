from django.conf import settings
from django.db import models

from products.models import Product


class Appointment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,
                             related_name='appointments')
    product = models.ForeignKey(Product,
                                on_delete=models.SET_NULL,
                                null=True,
                                related_name='appointments')
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return f'Your appointment is {self.date} at {self.time}. Don\'t forget your {self.product}'
