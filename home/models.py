from django.db import models
from .validators import file_size

# Create your models here.
class Video(models.Model):
    appname= models.CharField(max_length=20)
    description= models.CharField(max_length=100)
    url_playstore= models.CharField(max_length=100)
    video=models.FileField(upload_to="video/%y",validators=[file_size])
    def __str__(self):
        return self.appname

