from djongo import models
from django import forms


#
# class Blog(models.Model):
#     name = models.CharField(max_length=100)
#     tagline = models.TextField()
#
#     class Meta:
#         abstract = True
#
#
# class Entry(models.Model):
#     _id = models.ObjectIdField()
#     blog = models.EmbeddedField(
#         model_container=Blog,
#         # integrity check
#         null=False,
#         blank=False,
#     )
#     headline = models.CharField(max_length=255)
#     objects = models.DjongoManager()


# model form

class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    class Meta:
        abstract = True


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = (
            'name', 'tagline'
        )


class Entry(models.Model):
    blog = models.EmbeddedField(
        model_container=Blog,
        model_form_class=BlogForm
    )

    headline = models.CharField(max_length=255)
    objects = models.DjongoManager()

# operational
# from djongofields.embeddedfield.models import *
