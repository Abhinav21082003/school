from django.db import models

# Create your models here.
class stud(models.Model):
    s_name = models.CharField(max_length=30)
    s_class = models.CharField(max_length=30)
    s_addr = models.CharField(max_length=30)
    s_school = models.CharField(max_length=30)                       
    s_email = models.EmailField(max_length=30)
