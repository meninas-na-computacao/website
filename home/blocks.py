from wagtail.core import blocks
from wagtail.core.fields import StreamField
from wagtail.images.blocks import ImageChooserBlock


class PersonBlock(blocks.StreamBlock):
    image = ImageChooserBlock()
    name = blocks.TextBlock()

    class Meta:
        template = 'home/blocks/person.html'
