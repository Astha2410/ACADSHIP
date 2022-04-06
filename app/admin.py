from django.contrib import admin
from .models import App
from django.contrib.auth.admin import Group

# Register your models here.
admin.site.register(App)
admin.site.unregister(Group)

admin.site.site_header = "Acadship Admin"