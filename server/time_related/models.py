from django.db import models

# Create your models here.
from django.db.models import Model, CharField, DateTimeField
from django.contrib.postgres.fields import JSONField


class TimeRelatedObject(Model):
    """
    TimeRelatedObject
    """

    label = CharField("Label", max_length=64)
    start = DateTimeField("Start")
    end = DateTimeField("End")
    # "data = JSONField(null=True, blank=True)"

    @property
    def rec_type(self):
        return ""

    def __str__(self):
        return self.label
