from django.db import models
from datetime import date
from django.utils import timezone



# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length= 20)
    roll = models.IntegerField(primary_key= True)
    address = models.TextField()

    # big_auto_field = models.BigAutoField(primary_key=True)
    big_integer_field = models.BigIntegerField(default=0)
    binary_field = models.BinaryField(default=b'\x00')
    boolean_field = models.BooleanField(default=False)
    char_field = models.CharField(max_length=255, default='')
    date_field = models.DateField(default=date.today())
    date_time_field = models.DateTimeField(default=timezone.now)
    decimal_field = models.DecimalField(max_digits=5, decimal_places=2,default=0.00)
    duration_field = models.DurationField(default=timezone.timedelta(days=1))
    email_field = models.EmailField(default="")
    file_field = models.FileField(upload_to='files/', default="")
    # file_path_field = models.FilePathField(path='/path/to/files/')
    float_field = models.FloatField(default=0.0)
    generic_ip_address_field = models.GenericIPAddressField(default="0.0.0.0")
    






    def __str__(self):
        return f"roll:{self.roll} - {self.name}"