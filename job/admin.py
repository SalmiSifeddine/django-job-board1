from django.contrib import admin

# Register your models here.
from .models import job, category

admin.site.register(job)
admin.site.register(category)
