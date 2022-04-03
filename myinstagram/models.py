from django import db
from django.db import models
from django.contrib.auth.models import User

import datetime as dt

# Create your models here.
class Profile(models.Mode):
    class Meta:
        db_table='profile'

    bio=models.TextField(max_length=200,null=True,default='bio')
    profilepic=models.ImageField(upload_to='picture/',null=True,blank=True)
    user=models.OneToOneField(User, on_delete=models.CASCADE, blank=True, related_name="profile")
    followers = models.ManyToManyField(User, related_name="followers", blank=True)
    following = models.ManyToManyField(User, related_name="following", blank=True)

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def follow_user(self, follower):
        return self.following.add(follower)

    def unfollow_user(self, to_unfollow):
        return self.following.remove(to_unfollow)

    def is_following(self, checkuser):
        return checkuser in self.following.all()

    def get_number_of_followers(self):
        if self.followers.count():
            return self.followers.count()
        else:
            return 0

    def get_number_of_following(self):
        if self.following.count():
            return self.following.count()
        else:
            return 0

    @classmethod
    def search_users(cls, search_term):
        profiles = cls.objects.filter(user__username__icontains=search_term)
        return profiles

    def __str__(self):
        return self.user.username


class Location(models.Model):
    name = models.CharField(max_length=30)


    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    def __str__(self):
        return self.name


class tags(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    def save_tags(self):
        self.save()

    def delete_tags(self):
        self.delete()



        
