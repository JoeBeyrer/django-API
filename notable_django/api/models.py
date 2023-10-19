from django.db import models

# Create your models here.
#*******************************************************
# Model for a note - database fields will be limited to a 200 character title, 
# text field body, and a date time field for when the note was created
#*******************************************************
class Note(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s: %s' % (self.title, self.body)
