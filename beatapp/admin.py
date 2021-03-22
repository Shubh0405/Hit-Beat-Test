from django.contrib import admin
from .models import UserData,UserSound,BeatSound
# Register your models here.

admin.site.register(UserData)
admin.site.register(UserSound)
admin.site.register(BeatSound)
