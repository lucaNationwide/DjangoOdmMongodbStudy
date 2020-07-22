from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
from djongo import models
from django.core.validators import URLValidator


def script_injection(value):
    if value.find('<script>') != -1:
        raise ValidationError(_('Script injection in %(values)s'), params={'value': value})


class Address(models.Model):
    city = models.CharField(max_length=50)
    homepage = models.URLField(validators=[URLValidator, script_injection])

    class Meta:
        abstract = True


class Entry(models.Model):
    _id = models.ObjectIdField()
    address = models.EmbeddedField(model_container=Address, null=False, blank=False)
