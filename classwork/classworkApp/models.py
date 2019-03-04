from django.db import models
# Create your models here.

# calorie tracker model for the attributes required by read me

class CalTrackModel(models.Model):
    Username = models.CharField(max_length=200, default="")
    Calories = models.CharField(max_length=200, default="")
    Date = models.DateField(default = "")

    def __str__(self):
        return self.Username
