from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.documents.blocks import DocumentChooserBlock


class TitleAndTextBlock(blocks.StructBlock):
    """Title and text and nothing else."""

    title = blocks.CharBlock(required=True, help_text="Add your title")
    text = blocks.TextBlock(required=True, help_text="Add additional text")

    class Meta:  # noqa
        template = "streams/title_and_text_block.html"
        icon = "edit"
        label = "Title & Text"

from wagtail.core import blocks


class RichtextBlock(blocks.RichTextBlock):
    """Richtext with all the features."""

    class Meta:  # noqa
        template = "streams/richtext_block.html"
        icon = "doc-full"
        label = "Full RichText"


class SimpleRichtextBlock(blocks.RichTextBlock):
    """Richtext without (limited) all the features."""

    def __init__(
        self, required=True, help_text=None, editor="default", features=None, **kwargs
    ):  # noqa
        super().__init__(**kwargs)
        self.features = ["bold", "italic", "link"]

    class Meta:  # noqa
        template = "streams/richtext_block.html"
        icon = "edit"
        label = "Simple RichText"


class CardBlock(blocks.StructBlock):
    """Cards with image and text and button(s)."""

    title = blocks.CharBlock(required=True, help_text="Add your title")

    cards = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("image", ImageChooserBlock(required=True)),
                ("title", blocks.CharBlock(required=True, max_length=40)),
                ("text", blocks.TextBlock(required=True, max_length=200)),
                ("button_page", blocks.PageChooserBlock(required=False)),
                ("button_url", blocks.URLBlock(required=False, help_text="If the button page above is selected, that will be used first.")),
            ]
        )
    )

    class Meta:  # noqa
        template = "streams/card_block.html"
        icon = "placeholder"
        label = "Add Cards"



# -------------BLOCK FOR GR PAGE--------------
class ListAndButtonBlock(blocks.StructBlock):
    """List and buttons of main"""

    title = blocks.CharBlock(required=True)

    points = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("point", blocks.CharBlock(required=True, max_length=200)),
                ("pdfs", blocks.ListBlock(
                        DocumentChooserBlock(required=True),
                    )
                )
            ]
        )
    )

    class Meta:  #noqa
        template = "streams/list_and_button.html"
        icon="edit"
        label="GR Text & Documents"



# -------------BLOCK FOR RDE PAGE-------------
class ResourcesBlock(blocks.StructBlock):
    """List and buttons of main"""
    title = blocks.CharBlock(required=True)

    points = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("point", blocks.CharBlock(required=True, max_length=200)),
                ("url", blocks.URLBlock(required=True)),
            ]
        )
    )

    class Meta:  #noqa
        template = "streams/resources_page.html"
        icon="edit"
        label="Resources"


# -------------BLOCK FOR ABOUT US PAGE-------------

class participate_pointsBlock(blocks.StructBlock):

    text = blocks.CharBlock(required=True,max_length=255,null=True,blank=False)

    class Meta:
       template = "streams/participate_points.html"
       icon = "edit"
       label = "text"


# -------------BLOCKS FOR DOCUMENTATION AND PRESENTATIOON PAGE-------------

class DocumentBlock(blocks.StructBlock):
    """document block"""

    title = blocks.CharBlock(required=True)

    points = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("point", blocks.CharBlock(required=True, max_length=200)),
                ("doc_upload",DocumentChooserBlock(required=True)),
            ]
        )
    )

    class Meta:  #noqa
        template = "streams/document.html"
        icon="edit"
        label=" Documents"



class PresentationBlock(blocks.StructBlock):
    """document block"""
    
    image = ImageChooserBlock(icon="image")
    doc = DocumentChooserBlock(required=True)
    
   
    class Meta:  #noqa
        template = "streams/presentation.html"
        icon="edit"
        label="Presentation"


       