from django.db import models

class Message(models.Model):
    text = models.TextField()
    author = models.TextField()
    time = models.TimeField()

    def __str__(self):
        return self.text
