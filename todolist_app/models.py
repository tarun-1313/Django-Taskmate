from django.db import models
from django.conf import settings

class TaskList(models.Model):
    id =models.AutoField(primary_key=True)  
    manage = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None) 
    task = models.CharField(max_length=200)
    done = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['id']
    
    def __str__(self):
        return self.task + "-" + str(self.done)