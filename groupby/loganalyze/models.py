from django.db import models
from django.utils import timezone

"""
CREATE TABLE logs (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	date DATETIME,
	host VARCHAR,
	request VARCHAR,
	username VARCHAR
);

CREATE INDEX logs_host_IDX ON logs (host);
"""

# Create your models here.

class Log(models.Model):
    date = models.DateTimeField(default=timezone.now)
    host = models.CharField(max_length=128)
    request = models.CharField(max_length=128)
    username = models.CharField(max_length=128)

    class Meta:
        indexes = [
            models.Index(fields=["host"], name="host_idx")
        ]
    
