from django.db import models
from django.contrib.auth.models import User


class chatGroup(models.Model):
    group_name = models.CharField(max_length=255)

    def __str__(self):
        return self.group_name

class groupMessage(models.Model):
    group = models.ForeignKey(chatGroup, related_name="chat_messages", on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.CharField(max_length=300)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ["-created"]
    
    def __str__(self):
        return f"{self.author.username} : {self.body}"
    
