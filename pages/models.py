from django.db import models
from django.urls import reverse


# Create your models here.
class link(models.Model):
    redirect_link = models.URLField(max_length=200) 
    identifier = models.CharField(max_length=900, blank=True, null=True)

    def get_absolute_url(self):
        return reverse(
            'pages:url',
            args=[self.id]
        )