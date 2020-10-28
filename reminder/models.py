from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

# Create your models here.
class Details(models.Model):
    sno = models.AutoField(primary_key=True)
    detail = models.TextField()
    datetime = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.detail
    