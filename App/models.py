from django.db import models

# Create your models here.


class blobmodel(models.Model):
    title=models.CharField(max_length=122)
    desc=models.TextField(max_length=250)

    def __str__(self) -> str:
        return self.title