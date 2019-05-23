from wagtail.core import blocks
from wagtail.core.fields import StreamField
from wagtail.images.blocks import ImageChooserBlock
from django.utils.html import format_html, format_html_join


class PersonBlock(blocks.StructBlock):
    name = blocks.TextBlock()
    ocupation = blocks.TextBlock()
    image = ImageChooserBlock()
    description = blocks.TextBlock()
    extra = blocks.RichTextBlock(required=False)

    class Meta:
        template = 'blocks/person.html'


class PublicationBlock(blocks.StructBlock):
    title = blocks.TextBlock()
    author = blocks.TextBlock()
    place = blocks.TextBlock()
    link = blocks.TextBlock()

    class Meta:
        template = 'blocks/publication.html'


class ImageSquareBlock(blocks.StructBlock):
    image = ImageChooserBlock()
    text = blocks.TextBlock()
    description = blocks.TextBlock()

    class Meta:
        template = 'blocks/person.html'


class PersonListBlock(blocks.ListBlock):
    def render_basic(self, value, context=None):
        children = format_html_join(
            '\n', '{0}',
            [
                (self.child_block.render(child_value, context=context),)
                for child_value in value
            ]
        )
        return format_html("<div class=\"ui link cards\">{0}</div>", children)


class PublicationListBlock(blocks.ListBlock):
    def render_basic(self, value, context=None):
        children = format_html_join(
            '\n', '{0}',
            [
                (self.child_block.render(child_value, context=context),)
                for child_value in value
            ]
        )
        return format_html("<div class=\"ui items\">{0}</div>", children)
