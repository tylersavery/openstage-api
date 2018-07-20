from django.db import models
from django.contrib.auth.models import User

# Create your models here.

"""
Stage model
"""
class Stage(models.Model):
    
    STAGE_CHOICES = (
        ('music', 'Music'),
        ('comedy', 'Comedy'),
        ('poetry', 'Poetry'),
    )

    DAY_OF_WEEK_CHOICES = (
        ('mon', 'Monday'),
        ('tue', 'Tuesday'),
        ('wed', 'Wednesday'),
        ('thu', 'Thursday'),
        ('fri', 'Friday'),
        ('sat', 'Saturday'),
        ('sun', 'Sunday'),
    )

    kind = models.CharField(max_length=10, choices=STAGE_CHOICES)
    
    day_of_week = models.CharField(max_length=3, choices=DAY_OF_WEEK_CHOICES)
    start_time = models.TimeField()
    end_time = models.TimeField(null=True, blank=True)
    signup_time = models.TimeField(null=True, blank=True)

    signup_info = models.TextField(null=True, blank=True)
    included_gear = models.TextField(null=True, blank=True)

    thumb_image = models.ForeignKey('ImageAsset', related_name='thumb_image', null=True, blank=True, on_delete=models.SET_NULL)    
    images = models.ManyToManyField('ImageAsset', blank=True)

    venue_name = models.CharField(max_length=100)
    venue_address = models.CharField(max_length=100)
    venue_city = models.CharField(max_length=100)
    venue_state = models.CharField(max_length=100)
    venue_country = models.CharField(max_length=100)
    venue_latitude = models.DecimalField(max_digits=9, decimal_places=6)
    venue_longitude = models.DecimalField(max_digits=9, decimal_places=6)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "[%s] %s - %s " % (self.kind, self.day_of_week, self.venue_name)


"""
ImageAsset Model
"""
class ImageAsset(models.Model):
    url = models.CharField(max_length=255)
    width = models.IntegerField(default=0)
    height = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "[%d x %d] %s" % (self.width, self.height, self.url)


"""
RSVP model
"""
class Rsvp(models.Model):

    stage = models.ForeignKey('Stage', on_delete=models.CASCADE) 
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)   

    def __str__(self):
        return "[%s] %s" % (self.stage.venue_name, self.profile.user.username)


"""
Profile Model
"""

class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_performer = models.BooleanField(default=False)
    is_host = models.BooleanField(default=False)

    stages_performed_at = models.ManyToManyField('Stage', related_name='stages_performed_at', blank=True)
    stages_hosted_at = models.ManyToManyField('Stage', related_name='stages_hosted_at', blank=True)

    bio = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=32)

    avatar = models.ForeignKey('ImageAsset', blank=True, null=True, on_delete=models.SET_NULL)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)   

    def __str__(self):
        return self.user
