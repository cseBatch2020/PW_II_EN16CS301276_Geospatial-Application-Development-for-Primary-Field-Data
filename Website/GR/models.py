"""Government Resolutions"""

from django.db import models

from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from streams import blocks
from wagtail.search import index

class GRPage(Page):
    """GR Page Class"""

    template = "GR/govt_res_page.html"

    subtitle = models.CharField(max_length=100, null=True, blank=True)

    content = StreamField(
        [
            ("GR", blocks.ListAndButtonBlock()),
        ],
        null=True,
        blank=True,
        #label = "Main GR Docs",
    )

    content_panels = Page.content_panels + [
        FieldPanel("subtitle"),
        StreamFieldPanel("content"),
    ]

    class Meta: #noqa
        verbose_name = "Government Resolutions Page"
        verbose_name_plural = "Government Resolutions Pages"
