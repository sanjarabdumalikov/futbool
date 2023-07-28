
from django.db import models
from django.contrib.auth.models import AbstractUser
# from .managers import CustomUserManager
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.
class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('n','name'),
        ('a','addres'),
        ('c','contact')
    )

    USERNAME_FIELD = 'username'
    roles = models.CharField(max_length=1,choices=ROLE_CHOICES)
# Create your models here.

class Place(models.Model):
    name = models.CharField(max_length=50,default='')
    addres = models.CharField(max_length=50,default='')
    contact = models.CharField(max_length=50,default='')
    image = models.ImageField(upload_to='upolad/Place')
    booking_place_per_hour=models.IntegerField(default=0)
    # user = models.ForeignKey(User,on_delete=models.CASCADE,default=None,null=True)


    def str(self) -> str:
        return self.name
    class Meta:
        db_table="Place"
class Booking(models.Model):
    place = models.ForeignKey(Place,on_delete=models.CASCADE,null=True)
    starting_time = models.TimeField(default=datetime.now)
    ending_time = models.TimeField(default=datetime.now)
    start_free_time = models.TimeField(null=True, blank=True)
    class Meta:
        db_table="Place"