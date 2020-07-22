from django import forms
from djongo import models


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


class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Entry(models.Model):
    blog = models.EmbeddedField(
        model_container=Blog,
        model_form_class=BlogForm
    )
    meta_data = models.EmbeddedField(
        model_container=MetaData,
        model_form_class=MetaDataForm
    )

    headline = models.CharField(max_length=255)
    body_text = models.TextField()

    authors = models.ArrayReferenceField(
        to=Author,
        on_delete=models.CASCADE,
    )
    n_comments = models.IntegerField()

    def __str__(self):
        return self.headline
