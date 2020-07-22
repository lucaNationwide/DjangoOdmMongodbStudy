# require the closedsource version
from djongo.models.indexes import CompoundIndex
from djongo import models


class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    class Meta:
        indexes = [
            CompoundIndex(fields=['name', '-tagline'])
        ]
