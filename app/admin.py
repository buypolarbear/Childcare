from django.contrib import admin
from app.models import Child, Profile
# Register your models here.
admin.site.register([Child, Profile])
