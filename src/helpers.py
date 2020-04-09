from item import LightSource


def has_light_source(items):
    for item in items:
        if isinstance(item, LightSource):
            return True
    return False
