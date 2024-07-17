from django.contrib import admin
from .models import SpeedTestResult


class SpeedTestResultAdmin(admin.ModelAdmin):
    list_display = ('download_speed', 'upload_speed', 'host', 'timestamp')
# Register your models here.
admin.site.register(SpeedTestResult, SpeedTestResultAdmin)
