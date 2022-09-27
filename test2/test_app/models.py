from django.db import models
from datetime import datetime

# Create your models here.


class Machines(models.Model):
    event_id = models.AutoField(primary_key=True)
    status_1 = models.CharField(max_length=25)
    status_2 = models.CharField(max_length=25)
    dt_ts = models.DateTimeField(default=datetime.now())