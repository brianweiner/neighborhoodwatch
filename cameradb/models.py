from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


def validate_direction(value):
    acceptable_directions = ['N', 'NE', 'NW', 'S', 'SE', 'SW', 'E', 'W']
    if value not in acceptable_directions:
        raise ValidationError(
            _('%(value) is not a valid cardinal direction: N, E, S, W, or NE, NW, SE, SW'),
            params={'value': value},
        )

# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=200)
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=15)
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return '%s can be reached at %s or %s' % (self.name, self.contact_phone, self.contact_email)

    @receiver(post_save, sender=User)

    def update_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
        instance.profile.save()

class Location(models.Model):
    house_number = models.CharField(max_length=200)
    street = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE
    )
    def __str__(self):
        return '%s %s' % (self.house_number, self.street)

class Camera(models.Model):
    storage_duration = models.IntegerField()
    name = models.CharField(max_length=200)
    direction = models.CharField(max_length=2, validators=[validate_direction])
    location = models.ForeignKey(
        Location,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return '%s: facing %s - saves video for %s hours' % (self.name, self.direction, self.storage_duration)
