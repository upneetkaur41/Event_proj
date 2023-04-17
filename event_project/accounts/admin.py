from django.contrib import admin
from accounts.models import Profile
# Register your models here.
# admin.site.register(Events, Participants)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'age', 'address']

admin.site.register(Profile,ProfileAdmin)