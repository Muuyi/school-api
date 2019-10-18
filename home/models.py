from django.db import models

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=255)
    logo = models.FileField()
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name