from django.db import models
from django.utils import timezone

# Create your models here.

class LogMessage(models.Model):
    
    message = models.CharField(max_length= 300)
    log_date = models.DateTimeField("Date Logged")


    def __str__(self):
        """ Returns a string representation fo a message"""
        date = timezone.localtime(self.log_date)
        return f"'{self.message}' logged on {date.strftime('%A, %d %B, %Y at %X')}"