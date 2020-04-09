# Implement a class to hold room information. This should have name and
# description attributes.
from item import LightSource


class Room:
    def __init__(self, name, description, items=None, is_light=True):
        self.name = name
        self.description = description
        self.n_to = ''
        self.s_to = ''
        self.e_to = ''
        self.w_to = ''
        self.items = [] if items == None else items
        self.is_light = is_light

    def get_item(self, item):
        room_item = list(filter(lambda i: i.name == item, self.items))
        return room_item[0] if len(room_item) else False

    def remove_item(self, item):
        self.items = list(filter(lambda i: i.name != item, self.items))

    def add_item(self, item):
        self.items.append(item)

    def has_light_source(self):
        for item in self.items:
            if isinstance(item, LightSource):
                return True
        return False
