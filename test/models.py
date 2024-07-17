from django.db import models

class SpeedTestResult(models.Model):
    download_speed = models.FloatField()
    upload_speed = models.FloatField()
    host = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
