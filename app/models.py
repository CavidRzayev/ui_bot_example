from django.db import models
from user.models import User
# Create your models here.

class BaseModels(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    message = models.ManyToManyField("Message",db_index=True,blank=True)
    status = models.BooleanField(default=False,blank=True,null=True)

    def __str__(self) -> str:
        return str(self.date)


class Message(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    session_id = models.CharField(max_length=200,null=True,blank=True)
    quesion = models.CharField(max_length=500)
    answer = models.CharField(max_length=1000,blank=True,null=True)
    date = models.DateTimeField(auto_now_add=True,null=True)


    def __str__(self) -> str:
        return self.user.email



