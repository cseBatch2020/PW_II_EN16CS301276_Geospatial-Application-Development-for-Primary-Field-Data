from django.db import models

from wagtail.core.models import Page , Orderable
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, InlinePanel, StreamFieldPanel
from modelcluster.fields import ParentalKey
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.fields import RichTextField, StreamField
from streams import blocks


class HomePageCarouselImages(Orderable):
    """Between 1 and 5 images for the home page carousel."""

    page = ParentalKey("home.HomePage", related_name="carousel_images")
    carousel_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    carousel_image_title = models.CharField(max_length = 100,blank=False,null=True)
    carousel_image_information = RichTextField(features=['bold', 'italic'],null=True,blank=True,default="Carousel Image Information")

    panels = [
        ImageChooserPanel("carousel_image"),
        FieldPanel("carousel_image_title"),
        FieldPanel("carousel_image_information"),
        ]


class HomePage(Page):
    ''' home page model'''

    templates = "home/home_page.html"
    max_count = 1

    banner_title = models.CharField(max_length = 100,blank=False,null=True)
    banner_subtitle = models.CharField(max_length = 200,blank=False,null=True)
    vision_and_mission = models.TextField(null=True,blank=True,default="UMA Vision and Mission")
    logo_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    content = StreamField(
        [
            ("cards", blocks.CardBlock()),
        ],
        null=True,
        blank=True,
    )

    workshop_and_events = StreamField(
        [
            ("cards", blocks.CardBlock()),
        ],
        null=True,
        blank=True,
    )

    important_links = RichTextField(features=['link'],null=True,blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("banner_title"),
        FieldPanel("banner_subtitle"),
        ImageChooserPanel("logo_image"),

        MultiFieldPanel([
                InlinePanel("carousel_images", max_num=3, min_num=1, label="Image"),
            ],
            heading="Carousel Panel",
        ),
        FieldPanel("vision_and_mission"),

        MultiFieldPanel([
            StreamFieldPanel("content"),           
        ],heading="Participating Institutes"),

        FieldPanel("important_links"),

         MultiFieldPanel([
            StreamFieldPanel("workshop_and_events"),           
        ],heading="Workshop and events"),
     
    ]
