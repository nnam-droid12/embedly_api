from django.db import models

# Create your models here.

class SavedEmbed(models.Model):
    type = models.CharField(max_length=15, null=True)
    provider_url = models.URLField()
    provider_name = models.CharField(max_length=100, null=True)
    title = models.CharField(max_length=100, null=True)
    description = models.TextField()
    html = models.TextField()
    width = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    thumbnail_url = models.URLField()
    thumbnail_width = models.IntegerField(blank=True, null=True)
    thumbnail_height = models.IntegerField(blank=True, null=True)
    author_url = models.URLField()
    author_name = models.CharField(max_length=100, default='')
    version = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return str(self.provider_name)
