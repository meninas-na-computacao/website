from django.db import models

from wagtail.core.models import Page
from wagtail.core.blocks import ListBlock
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel,  StreamFieldPanel
from wagtail.core.fields import StreamField
from home import blocks


class HomePage(Page):
    body = RichTextField(blank=True)
    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
    ]


class SitePage(Page):
    body = RichTextField(blank=True)
    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
    ]


class SitePageRich(Page):
    body = StreamField([
        ('person', ListBlock(blocks.PersonBlock()))
    ])
    content_panels = Page.content_panels + [
        StreamFieldPanel('body', classname="full")
    ]
