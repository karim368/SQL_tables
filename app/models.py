from django.db import models

# Create your models here.

class Dept(models.Model):
    deptno = models.PositiveIntegerField(primary_key=True)
    dname = models.CharField(max_length=100)
    loc = models.CharField(max_length=100)

    def __str__(self):
        return self.dname
    
class Emp(models.Model):
    deptno = models.ForeignKey(Dept,on_delete=models.CASCADE)
    empno = models.PositiveIntegerField(primary_key=True)
    ename = models.CharField(max_length=100)
    job = models.CharField(max_length=100)
    mgr = models.PositiveIntegerField()
    sal = models.PositiveIntegerField()
    comm = models.PositiveIntegerField(null=True)
    hiredate = models.DateField()

    def __str__(self):
        return self.ename
