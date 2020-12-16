from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
import datetime

# Create your models here.


def validate_length(value):
    if value < 4:
        print("check hua check hua check hua check hua  check huacheck hua check hua check hua")
        raise ValidationError(
            _('%(value)s length is less than 4'),
            params={'value': value},
        )


class shortURL(models.Model):
    original_url = models.URLField(blank=False)
    short_url = models.CharField(blank=False, max_length=16)
    visits = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    last_visited = models.DateTimeField(auto_now_add=True)
