from dataclasses import Field
from datetime import date
from email.policy import default
from random import choices
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    img = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'


class AIProject(models.Model):
    projectTypes = (
        ('Text', 'Text'),
        ('Image', 'Image'),
    )
    siteTypes = (
        ('Corporate', 'Corporate'),
        ('E-Commerse', 'E-Commerse'),
        ('Blog', 'Blog'),
        ('Portfolio', 'Portfolio'),
        ('Wiki', 'Wiki'),
    )
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    projectType = models.CharField(max_length=15, choices=projectTypes)
    purpose = models.CharField(max_length=15, choices=siteTypes)
    date = models.DateField(default=timezone.now)
    homePage = models.BooleanField()
    aboutPage = models.BooleanField()
    contactPage = models.BooleanField()
    customPage = models.BooleanField()
    customPageName = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return f'{self.name} - {self.creator}'
