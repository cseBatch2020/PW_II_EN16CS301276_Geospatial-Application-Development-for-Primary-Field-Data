from django.db import models
from wagtail.images.blocks import ImageChooserBlock
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, PageChooserPanel
from wagtail.core.fields import StreamField
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.images.edit_handlers import ImageChooserPanel
# from wagtailimages.blocks import ImageChooserBlock
from streams import blocks
from workshop import dayfield
from django.utils import timezone
# from workshop.models import Event
# Create your models here.
# from wagtail.core.blocks import DateTimeBlock
# from datetime import datetime

class WorkshopListingPage(Page):
    """Listing page lists all the Blog Detail Pages."""

    template = "workshop/workshop_listing_page.html"

    custom_heading = models.CharField(
        max_length=100,
        blank=False,
        null=False,
        help_text='Overwrites the default title',
    )
    
    content_panels = Page.content_panels + [
        FieldPanel("custom_heading"),
    ]

    def get_context(self, request, *args, **kwargs):
        """Adding custom stuff to our context."""
        context = super().get_context(request, *args, **kwargs)
        context["posts"] = WorkshopDetailPage.objects.live().public()
        # context["p_posts"] = PastWorkshopDetailPage.objects.live().public()
        return context


class WorkshopDetailPage(Page):
    """Workshop detail page."""

    template = "workshop/workshop_detail_page.html"

    type_of_workshop = dayfield.TypesOfWorkshopsField(blank=False, null=True)

    custom_title = models.CharField(
        max_length=100,
        blank=False,
        null=False,
        help_text='Overwrites the default title',
    )

    blog_image = models.ForeignKey(
        "wagtailimages.Image",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
    )

    short_desc = models.CharField(max_length=100)

    content = StreamField(
        [
            ("description", blocks.DescriptiveRichtextBlock()),
        ],
        null=True,
        blank=True,
    )

    date_of_event = models.DateField(blank=False, null=True)

    time_of_event = models.TimeField(blank=False, null=True)

    day_of_event = dayfield.DayOfTheWeekField(blank=False, null=True)

    address = models.CharField(max_length=300)

    content_panels = Page.content_panels + [
        FieldPanel("type_of_workshop"),
        FieldPanel("custom_title"),
        ImageChooserPanel("blog_image"),
        FieldPanel("short_desc"),
        StreamFieldPanel("content"),       
        FieldPanel("date_of_event"),
        FieldPanel("time_of_event"),
        FieldPanel("day_of_event"),
        FieldPanel("address"),
        
        # StreamFieldPanel("contents"),
    ]

 