from django.db import models

class Array(models.Model):
    user = models.CharField(max_length=100, default="user")
    body = models.CharField(max_length=3000, default="body")

class Push(models.Model):
    user = models.CharField(max_length=100, default="user")
    push = models.CharField(max_length=1000, default="push")
    array = models.ForeignKey(Array, on_delete=models.CASCADE, related_name="push", null=True, blank=True)
    # class Meta:
    #     unique_together = ['user', 'push']
    # def __str__(self):
    #     return '%d: %s' % (self.user, self.push)

class Profile(models.Model):
    firstname = models.CharField(max_length=100, default='')
    lastname = models.CharField(max_length=100, default='')
    genderpronouns = models.CharField(max_length=100, default='')
    location = models.CharField(max_length=100, default='')
    aboutme = models.CharField(max_length=500, default='')
    linkedin = models.CharField(max_length=100, default='')