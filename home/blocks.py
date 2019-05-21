from wagtail.core import blocks
from wagtail.core.fields import StreamField
from wagtail.images.blocks import ImageChooserBlock


class PersonBlock(blocks.StructBlock):
    name = name = blocks.TextBlock()
    image = ImageChooserBlock()

    class Meta:
        template = 'blocks/person.html'
