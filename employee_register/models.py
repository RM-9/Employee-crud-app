from django.db import models

# Create your models here.

class Position(models.Model):
    role=models.CharField(max_length=30)
    
    def __str__(self):
        return self.role
    
class Employee(models.Model):
    name=models.CharField(max_length=30)
    emp_id=models.CharField(max_length=30)
    mobile=models.CharField(max_length=10)
    position=models.ForeignKey(Position,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

