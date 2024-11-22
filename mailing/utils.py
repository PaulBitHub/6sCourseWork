NULLABLE = {"blank": True, "null": True}


def upload_to(instance, filename):
    """
    Создает путь загрузки файла на основе типа модели
    """
    return f"uploads/{instance.__class__.__name__.lower()}/{filename}"
