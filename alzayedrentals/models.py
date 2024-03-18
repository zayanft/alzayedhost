from django.db import models

# Create your models here.
# Home Slide Models

class home_slide(models.Model):
    image1= models.ImageField(upload_to='homepage')
    image2 = models.ImageField(upload_to='homepage')
    image3 = models.ImageField(upload_to='homepage')


    

# EQUIPMENTS
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Equipment(models.Model):
    image = models.ImageField(upload_to="equipments")
    EQUIPMENT_TYPES = (
        ('EXCAVATOR', 'EXCAVATOR'),
        ('CRANES', 'CRANES'),
        ('CLEANING EQUIPMENT', 'CLEANING EQUIPMENT'),
        ('LIFTING EQUIPMENT', "LIFTING EQUIPMENT"),
        ('TRUCK','TRUCK'),
        ('TANKER','TANKER'),
        ('POWER TOOLS','POWER TOOLS'),
        ('PUMP','PUMP'),
        ('CONSTRUCTION EQUIPMENTS','CONSTRUCTION EQUIPMENTS'),
    )
    type = models.CharField(max_length=50,choices=EQUIPMENT_TYPES, default='EXCAVATOR')

    title = models.CharField(max_length=80)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return self.title

class Service(models.Model):
    image = models.ImageField(upload_to='services')
    title = models.CharField(max_length=50)
    description = models.TextField(null=False)

    def __str__(self):
        return self.title