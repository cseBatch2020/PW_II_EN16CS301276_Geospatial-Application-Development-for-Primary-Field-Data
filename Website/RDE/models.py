from django.db import models

from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from streams import blocks

class RDEPage(Page):
    """GR Page Class"""

    template = "RDE/RDE_page.html"

    subtitle = models.CharField(max_length=100, null=True, blank=True)

    content = StreamField(
        [
            ("resources", blocks.ResourcesBlock()),
            # ("essays", blocks.EssaysBlock()),
            # ("materials", blocks.MaterialsBlock()),
            # ("links", blocks.LinksBlock()),
        ],
        null=True,
        blank=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel("subtitle"),
        StreamFieldPanel("content"),
    ]

    class Meta: #noqa
        verbose_name = "Resources for Development and Engineering Page"
        verbose_name_plural = "Resources for Development and Engineering Pages"
