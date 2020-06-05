from django.db import models
from wagtail.images.blocks import ImageChooserBlock
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core.fields import StreamField
from wagtail.documents.blocks import DocumentChooserBlock
# from wagtailimages.blocks import ImageChooserBlock
from streams import blocks

class DocumentPage(Page):
    template = "Docs_Presentations/document_page.html"
    content = StreamField(
		[
			("doc_upload",blocks.DocumentBlock())
		],
		null=True,
		blank=True,
	) 

    contents = StreamField(
		[
			("doc",blocks.PresentationBlock())

		],
    null=True,
		blank=True,
  )
    content_panels = Page.content_panels + [
         
         StreamFieldPanel("content"),
         StreamFieldPanel("contents"),
        
      ]

    class Meta:
         verbose_name = "Presentation and Document Page" 
 

