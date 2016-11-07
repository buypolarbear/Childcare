from django.contrib import admin
from app.models import Child, Profile, CheckIn_Log
# Register your models here.
admin.site.register([Child, Profile, CheckIn_Log])
