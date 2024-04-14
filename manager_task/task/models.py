from django.db import models
from django.utils import timezone
# Create your models here.

class Job(models.Model):
    job_name =  models.CharField(max_length=20 , null=True)
    describe = models.CharField(max_length=200, null=True)
    # date = models.DateTimeField(auto_now_add=True)


    
class User(models.Model):
    user_name = models.CharField(max_length=20 , null=True)
    school_name = models.CharField(max_length=200 ,null=True)
    address = models.CharField(max_length=200 , null=True)
    # date_of_birth = models.DateTimeField(auto_now_add=True)
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='job')
    def __str__(self):
        return str(self.job)
    
