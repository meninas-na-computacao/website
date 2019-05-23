from django.db import models

from wagtail.core import blocks as wg_blocks
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import FieldPanel,  StreamFieldPanel
from wagtail.contrib.table_block.blocks import TableBlock
from home import blocks, table_opt


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
    body = RichTextField(blank=True)
    extra = StreamField([
        ('person', blocks.PersonListBlock(blocks.PersonBlock())),
        ('publication',  blocks.PublicationListBlock(blocks.PublicationBlock())),
        ('table', TableBlock(table_options=table_opt.TABLE_OPTIONS)),
        ('rich', wg_blocks.RichTextBlock())
    ])
    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
        StreamFieldPanel('extra', classname="full")
    ]
