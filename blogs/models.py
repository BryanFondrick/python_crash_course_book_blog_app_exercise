from django.db import models

# Create your models here.

class BlogPost(models.Model):
    """A user titled blog with text"""
    title = models.CharField(max_length=40)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    #date_added = models.DateTimeField(default=datetime.now, blank=True); from datetime import datetime
    
    def __str__(self):
        """Return a string representation of the model."""
        return self.title
