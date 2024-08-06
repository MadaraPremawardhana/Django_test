from os import name
from django.db import models
from django.utils import timezone

class LogMessage(models.Model):
    title = models.CharField(max_length=100)
    message = models.TextField()
    log_date = models.DateTimeField()
    
    def to_dict(self):
       return { 'id': self.id, 'title': self.title, 'message': self.message}
    def __str__(self):
        return "id:"+ str(self.id)+", title:"+ self.title+ "message:"+ self.message

class Student(models.Model):
    id =models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    UG = models.BooleanField()