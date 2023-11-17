from django.db import models

class SenosrInstance(models.Model):
    name=models.CharField(max_length=200,unique=True,null=False,blank=False)
    connected=models.BooleanField(default=False,null=True,blank=True)
    time=models.DateTimeField(auto_now_add=True)
    last_updated=models.DateTimeField(null=True,blank=True)
    
    def __str__(self):
        return self.name
