from django.db import models

# Create your models here.

class Thing(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank = True)
    quantity = models.IntegerField()
    creation_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title

    def Meta(self):
        ordering['title']



