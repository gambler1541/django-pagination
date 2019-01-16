from django.db import models
from django.views.generic import ListView


class Constacts(models.Model):
    text = models.TextField(default='')


