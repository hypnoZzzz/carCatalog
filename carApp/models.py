import uuid

from django.db import models
from django.urls import reverse


class Car(models.Model):
    """Описание автомобиля"""
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    brand = models.CharField(max_length=15,
                             verbose_name="марка автомобиля")
    car_model = models.CharField(max_length=10,
                                 verbose_name="модель автомобиля")
    year_of_issue = models.SmallIntegerField(verbose_name="год выпуска",
                                             default=2018)

    MECHANIC = 1
    AUTOMATIC = 2
    ROBOT = 3
    TRANSMISSION_CHOICES = [
        (MECHANIC, 'Механика'),
        (AUTOMATIC, 'Автомат'),
        (ROBOT, 'Робот')
    ]
    transmission = models.SmallIntegerField(default=MECHANIC,
                                            choices=TRANSMISSION_CHOICES)
    color = models.CharField(max_length=25,
                             verbose_name="цвет автомобиля")
    photo = models.ImageField(upload_to='cars_photo', blank=True)

    def __str__(self):
        return "{} ({}, {})".format(self.brand, self.car_model, self.color)

    def get_absolute_url(self):
        return reverse('car_detail', kwargs={'pk': self.pk})
