# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.TextField()
    kr_desc = models.TextField()
    en_desc = models.TextField()
    startdate = models.DateField()
    enddate = models.DateField()
    poster = models.ImageField()
    examples = models.FileField(default=None, null=True)
    pdf_file = models.FileField(default=None, null=True)

    def __str__(self):
        return self.title
