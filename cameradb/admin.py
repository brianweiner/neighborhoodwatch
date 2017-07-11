from django.contrib import admin

from .models import Camera, Location, Profile

admin.site.register(Camera)

class CameraInline(admin.TabularInline):
    model = Camera

class LocationAdmin(admin.ModelAdmin):
    inlines = [
        CameraInline,
    ]

class LocationInline(admin.TabularInline):
    model = Location

class ProfileAdmin(admin.ModelAdmin):
    inlines = [
        LocationInline,
    ]

admin.site.register(Location, LocationAdmin)
admin.site.register(Profile, ProfileAdmin)
