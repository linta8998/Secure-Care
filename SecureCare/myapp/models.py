from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Login(AbstractUser):
    user_type=models.CharField(max_length=30,default="member")
    view_password=models.CharField(max_length=30)
    def __str__(self):
        return self.user_type
    

class Residents(models.Model):
    name=models.CharField(max_length=100)
    age=models.CharField(max_length=100)
    gender=models.CharField(max_length=100,null=True)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    address=models.CharField(max_length=100,null=True)
    image = models.FileField(upload_to="file", null= True)

class CareTaker(models.Model):
    login=models.ForeignKey(Login,on_delete=models.CASCADE,null=True)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100,null=True)
    phone=models.CharField(max_length=100)
    address=models.CharField(max_length=100,null=True)
    image = models.FileField(upload_to="file", null= True)

class Nurse(models.Model):
    login=models.ForeignKey(Login,on_delete=models.CASCADE,null=True)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100,null=True)
    phone=models.CharField(max_length=100)
    address=models.CharField(max_length=100,null=True)
    image = models.FileField(upload_to="file", null= True)

class Doctor(models.Model):
    login=models.ForeignKey(Login,on_delete=models.CASCADE,null=True)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100,null=True)
    phone=models.CharField(max_length=100)
    address=models.CharField(max_length=100,null=True)
    image = models.FileField(upload_to="file", null= True)
    

class WeightChart(models.Model):
    resident=models.ForeignKey(Residents,on_delete=models.CASCADE,null=True)
    weight=models.CharField(max_length=100)
    month=models.CharField(max_length=100)
    year=models.CharField(max_length=100)


class FoodTimeTable(models.Model):
    resident=models.ForeignKey(Residents,on_delete=models.CASCADE,null=True)
    day=models.CharField(max_length=100)
    meal=models.CharField(max_length=100)
    menu=models.CharField(max_length=100)


class Medicine(models.Model):
    resident=models.ForeignKey(Residents,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=100,null=True)
    dosage=models.CharField(max_length=100,null=True)
    frequency=models.CharField(max_length=100,null=True)
    bf_af=models.CharField(max_length=100,null=True)
    notes=models.CharField(max_length=100,null=True)
            
    
class CarePlan(models.Model):
    resident=models.ForeignKey(Residents,on_delete=models.CASCADE,null=True)
    likeOrdislike=models.CharField(max_length=100,null=True)
    note=models.CharField(max_length=100,null=True)                    
            
    
class EmergencySituation(models.Model):
    resident = models.ForeignKey(Residents,on_delete=models.CASCADE,null=True)
    situation = models.CharField(max_length=100,null=True)
    status = models.CharField(max_length=100,null=True)    
    file = models.FileField(upload_to="file", null= True)
    reply = models.CharField(max_length=100,null=True)    
        
        

class Chat(models.Model):
    uid = models.ForeignKey(Nurse, on_delete=models.CASCADE)
    artistid = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    message = models.CharField(max_length=300)
    date = models.DateField(auto_now=True)
    time = models.CharField(max_length=100)
    utype = models.CharField(max_length=100)
        