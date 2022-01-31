from django.db import models

from django.contrib.auth.models import User


# Create your models here.

class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name
 
class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    participants = models.ManyToManyField(
        User, related_name='participants', blank=True)
    updated = models.DateTimeField(auto_now=True) # takes a snapshot of the instance everytime its saved
    created = models.DateTimeField(auto_now_add=True) # takes a snapshot of the instance just when it's created

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self) -> str:
        return self.name



class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) # Django has a base model for user. Check documentation for more information
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True) # takes a snapshot of the instance everytime its saved
    created = models.DateTimeField(auto_now_add=True) # takes a snapshot of the instance just when it's created

    class Meta:
        ordering = ['-updated', '-created']


    def __str__(self) -> str:
        if len(self.body) < 50:
            return self.body
        return self.body[0:50] + '...'
        

