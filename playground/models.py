from django.db import models

class members(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.IntegerField(null=True)
    date_join = models.DateField(null=True)
    salary = models.IntegerField(null=True)
    bonus = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    
    @property
    def total(self):
        return self.salary + self.bonus
    
    @staticmethod
    def valid_salary(salary):
        return salary > 0
    
    @classmethod
    def desig(cls, name, join, designation):
        record = cls(name=name, join=join)
        record.designation = designation
        return designation
    
    def __str__(self):
        return f'{self.firstname} {self.lastname}'
    
