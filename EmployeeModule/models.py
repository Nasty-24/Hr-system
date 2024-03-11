from django.db import models

# Create your models here.
class Employee(models.Model):
    full_name = models.CharField(max_length=50)
    email = models.EmailField()
    emp_code = models.IntegerField()
    mobile = models.IntegerField()
    position = models.IntegerField()
    def __str__(self):
        return self.full_name

