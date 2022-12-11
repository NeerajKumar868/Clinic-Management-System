from django.db import models
from django.contrib.auth.models import User,Group

# Create your models here.


admin,status = Group.objects.get_or_create(name='admin')
customer,status = Group.objects.get_or_create(name='customer')

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username