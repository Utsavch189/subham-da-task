from django.db import models
from datetime import datetime

class People(models.Model):
    people_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=255)
    age=models.PositiveIntegerField()
    registered_at=models.DateTimeField(default=datetime.now())

    def __str__(self) -> str:
        return self.name