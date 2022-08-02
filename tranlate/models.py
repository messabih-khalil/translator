from django.db import models

# Create your models here.


class Trans(models.Model):
    
    noun=models.CharField(max_length=100)
    datebirth=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    nationality=models.CharField(max_length=100)
    
    class Meta :
         db_table='data'

    def __str__(self):
        return self.Noun