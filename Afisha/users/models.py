from django.contrib.auth.models import User
from django.db import models


class SMSCode(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE, related_name='sms_code')
    code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.code
