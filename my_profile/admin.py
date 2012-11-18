from django.contrib import admin
from my_profile.models import MyProfile, Photo

class ProfileAdmin(admin.ModelAdmin):
	pass

class PhotoAdmin(admin.ModelAdmin):
	pass

admin.site.register(MyProfile, ProfileAdmin)
admin.site.register(Photo, PhotoAdmin)