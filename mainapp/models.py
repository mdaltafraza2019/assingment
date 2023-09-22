from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=100)
    dob=models.DateField()
    mob=models.CharField(max_length=15)
    email=models.EmailField()
    pic=models.ImageField(upload_to='media/',default=None,null=True,blank=True)

    def __str__(self):
        return self.name
