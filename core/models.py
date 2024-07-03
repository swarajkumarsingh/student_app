from django.db import models
from django.core.validators import validate_email


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    full_name = models.CharField(max_length=10000)
    contact_phone = models.CharField(max_length=12)
    contact_mail = models.EmailField(validators=[validate_email])

    class Meta:
        verbose_name_plural = 'Student'    

    def __str__(self):
        return self.contact_mail
