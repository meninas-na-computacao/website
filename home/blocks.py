from wagtail.core import blocks
from wagtail.core.fields import StreamField
from wagtail.images.blocks import ImageChooserBlock


class PersonBlock(blocks.StructBlock):
    name = blocks.TextBlock()
    image = ImageChooserBlock()
    description = blocks.RichTextBlock()

    class Meta:
        template = 'blocks/person.html'


class PublicationBlock(blocks.StructBlock):
    title = blocks.TextBlock()
    author = blocks.TextBlock()
    place = blocks.TextBlock()

    class Meta:
        template = 'blocks/person.html'


class ImageSquareBlock(blocks.StructBlock):
    image = ImageChooserBlock()
    text = blocks.TextBlock()
    description = blocks.TextBlock()

    class Meta:
        template = 'blocks/person.html'
