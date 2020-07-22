from django.views.generic import DetailView
from djongo import models


class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    class Meta:
        abstract = True


class Entry(models.Model):
    blog = models.EmbeddedField(
        model_container=Blog,
    )
    headline = models.CharField(max_length=255)
    objects = models.DjongoManager()


class EntryView(DetailView):

    def get_object(self, queryset=None):
        index = [i for i in Entry.objects.mongo_aggregate(
            [
                {
                    '$match': {
                        'headline': self.kwargs['path']
                    }
                },
            ])]
        return index
