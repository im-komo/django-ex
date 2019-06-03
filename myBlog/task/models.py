from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.
class Task(models.Model):
    TAGS = (('T', 'Technology'), ('F', 'Food'))
    title = models.CharField(max_length=200)
    text = models.TextField()
    tags = models.CharField(max_length=1, choices=TAGS)
    created_date = models.DateTimeField(default=timezone.now)
    iscompleted = models.BooleanField(default=False)

    def __str__(self):
        return self.title