from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=User)
    title = models.CharField(max_length=50)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True, blank=True, upload_to='images/')

    def __str__(self):
        return self.title + ' | ' + str(self.user)

    class Meta:
        ordering = ['-created']


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(null=True, blank=True, upload_to='images/profile')
    car = models.CharField(max_length=100, null=True, blank=True)
    mods = models.TextField(null=True, blank=True)
    pic_1 = models.ImageField(null=True, blank=True, upload_to='images/profile')
    pic_2 = models.ImageField(null=True, blank=True, upload_to='images/profile')
    pic_3 = models.ImageField(null=True, blank=True, upload_to='images/profile')

    def __str__(self):
        return str(self.user)