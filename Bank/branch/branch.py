from django.db import models

# Create your models here.
class Branch(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=25)
    loc=models.TextField(blank=True)

    def __str__(self):
        return f"{self.id}  {self.name}"