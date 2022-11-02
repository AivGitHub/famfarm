import pathlib

from django import template

from account.models import User


register = template.Library()


@register.simple_tag
def get_thumbnail(avatar):
    if not avatar:
        return

    original_path = pathlib.Path(avatar.url)

    return original_path.parent.joinpath(
        '%s_%s%s' % (
            original_path.stem,
            User.THUMBNAIL_PREFIX,
            original_path.suffix
        )
    )
