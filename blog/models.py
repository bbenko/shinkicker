from django.db import models
from datetime import datetime
from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import slugify

DRAFT = 1
PUBLISHED = 2
STATUS_CHOICES = (
    (DRAFT, _("Draft")),
    (PUBLISHED, _("Published")),
)


class Post(models.Model):
    title = models.CharField(_("Title"), max_length=256)
    slug = models.SlugField()
    content = models.TextField(_("Content"))
    status = models.IntegerField(_("Status"), choices=STATUS_CHOICES, default=DRAFT)
    published = models.DateTimeField(_("Published"), default=datetime.now)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    class Meta:
        ordering = ["-published", ]

    def __unicode__(self):
        return self.title
