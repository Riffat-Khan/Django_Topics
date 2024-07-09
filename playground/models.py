from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    ROLE_CHOICES = [
        ('manager', 'Manager'),
        ('qa', 'QA'),
        ('developer', 'Developer'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    role = models.CharField(max_length=100, choices=ROLE_CHOICES)
    contact_number = models.CharField(max_length=15)

    # def __str__(self):
    #     return self.user.username

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(null=True)
    team_members = models.ManyToManyField(Profile)
    
class Task(models.Model):
    STATUS_CHOICES = [
        ('open', 'Open'),
        ('review', 'Review'),
        ('working', 'Working'),
        ('awaiting release', 'Awaiting Release'),
        ('waitingg qa', 'Waitingg QA'),
    ]
    
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=100, choices=STATUS_CHOICES)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    assignee = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    
class Document(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    file = models.FileField(upload_to='documents/', null=True, blank=True)
    version = models.CharField(max_length=100)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    
class Comment(models.Model):
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

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
    
