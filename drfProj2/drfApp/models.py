from django.db import models

# Create your models here.

class Platform(models.Model):
    name=models.CharField(max_length=20)
    website=models.URLField()

    def __str__(self):
        return self.name
    

class Show(models.Model):
    title=models.CharField(max_length=40)
    released_on=models.DateField()
    rating=models.FloatField()
    streaming_platform=models.ForeignKey(Platform, on_delete=models.CASCADE, related_name="shows_available")

    def __str__(self):
        return self.title
