def get_avatar_path(instance, filename: str) -> str:
    return f'data/avatars/user_{instance.pk}/{filename}'


def get_photo_path(instance, filename: str) -> str:
    return f'data/uploads/album_{instance.pk}/{filename}'
