from django.db import models

from user_app.models import User

# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    task = models.CharField(max_length=100)

    created_date = models.DateTimeField(auto_now_add=True)  

    is_completed = models.BooleanField(default=False)

    priority = models.Choices("high","low") 