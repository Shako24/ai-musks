from django.db import models
from custom.models import AIProject
import os

# Create your models here.


def get_upload_path(instance, filename):
    return os.path.join('pageImages', 'imageInput', instance.parent.creator.username, instance.parent.name, instance.pageName, filename)


class ImagePage(models.Model):
    pageTypes = (
        ('Home', 'Home'),
        ('About', 'About'),
        ('Contact', 'Contact'),
        ('Custom', 'Custom'),
    )
    parent = models.ForeignKey(AIProject, on_delete=models.CASCADE)
    pageType = models.CharField(max_length=15, choices=pageTypes)
    pageName = models.CharField(max_length=25, default='Custom')
    img = models.ImageField(default='default.jpg', upload_to=get_upload_path)
    made = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.pageName}, {self.id} : {self.parent.id} - {self.parent.name}, {self.parent.creator}'s Image Project"
