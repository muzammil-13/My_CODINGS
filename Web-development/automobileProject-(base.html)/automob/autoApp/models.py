from django.db import models
# from django.db.models.deletion import CASCADE


# Create your models here.
class Vehicle(models.Model):
    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to='pics')
    descr = models.TextField()

    def __str__(self):
        return '{}'.format(self.name)
