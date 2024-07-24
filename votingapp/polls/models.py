# yourapp/models.py

from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True, max_length=255)
    password = models.CharField(max_length=255)
    username= models.CharField(max_length=255,default="")
    
class UserProfile(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    gender = models.BooleanField()

   
class Event(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=244)
    candidates = models.ManyToManyField('Candidate', related_name='events')
    expiration_date = models.DateTimeField()

    def __str__(self):
        return self.title

class Candidate(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_vote = models.IntegerField(default=0)
    
    def __str__(self):
        return f"Candidate: {self.user.email}"

class Voted(models.Model):
    the_voted = models.ForeignKey(User, on_delete=models.CASCADE)
    the_candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True) 
    Event = models.ForeignKey(Event, on_delete=models.CASCADE)   

    def __str__(self):
      return f"Event: {self.event.title}, Candidate: {self.candidate.user.email}"