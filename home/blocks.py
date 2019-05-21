from wagtail.core import blocks
from wagtail.core.fields import StreamField
from wagtail.images.blocks import ImageChooserBlock


class PersonBlock(blocks.StructBlock):
    name = blocks.TextBlock()
    image = ImageChooserBlock()
    description = blocks.RichTextBlock()

    class Meta:
        template = 'blocks/person.html'
