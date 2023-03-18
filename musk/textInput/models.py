from django.db import models
from custom.models import AIProject
import os

# Create your models here.


# def filePath(instance, filename):
#     return os.path.join('..', 'textInput', 'static', 'outputHTML', instance.parent.creator.username, instance.parent.name, filename)


class TextPage(models.Model):
    pageTypes = (
        ('Home', 'Home'),
        ('About', 'About'),
        ('Contact', 'Contact'),
        ('Custom', 'Custom'),
    )
    parent = models.ForeignKey(AIProject, on_delete=models.CASCADE)
    pageType = models.CharField(max_length=15, choices=pageTypes)
    pageName = models.CharField(max_length=25, default='Custom')
    heading = models.IntegerField(default=0, blank=True, null=True)
    navbar = models.IntegerField(default=0, blank=True, null=True)
    textbox = models.IntegerField(default=0, blank=True, null=True)
    paragraph = models.IntegerField(default=0, blank=True, null=True)
    image = models.IntegerField(default=0, blank=True, null=True)
    button = models.IntegerField(default=0, blank=True, null=True)
    checkbox = models.IntegerField(default=0, blank=True, null=True)
    dropdown = models.IntegerField(default=0, blank=True, null=True)
    footer = models.IntegerField(default=0, blank=True, null=True)
    label = models.IntegerField(default=0, blank=True, null=True)
    textarea = models.IntegerField(default=0, blank=True, null=True)
    link = models.IntegerField(default=0, blank=True, null=True)
    colorScheme = models.TextField(null=True, blank=True)
    made = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.pageName}, {self.id} : {self.parent.id} - {self.parent.name}, {self.parent.creator}'s Text Project"


def get_upload_path(instance, filename):
    return os.path.join('pageImages', 'textInput', instance.textpage.parent.creator.username, instance.textpage.parent.name, instance.textpage.pageName, filename)


class TextPageImage(models.Model):
    textpage = models.ForeignKey(TextPage, on_delete=models.CASCADE)
    pic = models.ImageField(default='default.jpg', upload_to=get_upload_path)

    def __str__(self):
        return f"{self.textpage.parent.creator.username}, {self.textpage.parent.name}, {self.textpage.pageName}, {self.pic}"
