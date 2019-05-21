from django.db import models

from wagtail.core.models import Page
from wagtail.core.blocks import ListBlock
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel,  StreamFieldPanel
from wagtail.contrib.table_block.blocks import TableBlock
from wagtail.core.fields import StreamField
from home import blocks, table_opt

from wagtail.core import blocks as wg_blocks


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
        ('person', ListBlock(blocks.PersonBlock())),
        ('publication', ListBlock(blocks.PublicationBlock())),
        ('table', TableBlock(table_options=table_opt.TABLE_OPTIONS)),
        ('rich', wg_blocks.RichTextBlock())
    ])
    content_panels = Page.content_panels + [
        StreamFieldPanel('body', classname="full")
    ]
