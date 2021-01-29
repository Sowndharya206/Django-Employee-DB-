from django.db import models

# Create your models here.
class Emp(models.Model):
    eid=models.IntegerField()
    ename=models.CharField(max_length=20)
    eemail=models.EmailField()
    econtact=models.CharField(max_length=15)
    elocation=models.CharField(max_length=20)
    class Meta:
        db_table="emp"