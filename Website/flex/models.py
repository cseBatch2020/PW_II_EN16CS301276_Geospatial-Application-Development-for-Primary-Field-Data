from django.db import models
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel , StreamFieldPanel
from streams import blocks
from wagtail.core.fields import StreamField

# Create your models here.

class FlexPage(Page):

    template = "flex/flex_page.html"
    subtitle = models.CharField(max_length= 100, null = True , blank = True)

    content_panels = Page.content_panels + [
        FieldPanel("subtitle"),
        StreamFieldPanel("content"),
    ]

    content = StreamField(
        [
            ("title_and_text", blocks.TitleAndTextBlock()),
            ("full_richtext", blocks.RichtextBlock()),
            ("simple_richtext", blocks.SimpleRichtextBlock()),
        ],
        null=True,
        blank=True,
    )

    class Meta: # noqa
        verbose_name = "Flex Page"
        verbose_name_plural = "Flex Pages"