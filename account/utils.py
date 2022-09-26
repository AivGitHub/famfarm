def avatar_path(instance, filename: str) -> str:
    return f'data/avatars/user_{instance.pk}/{filename}'


def photo_path(instance, filename: str) -> str:
    return f'data/uploads/user_{instance.pk}/{filename}'
