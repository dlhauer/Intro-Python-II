# Write a class to hold player information, e.g. what room they are in
# currently.
from item import LightSource


class Player:
    def __init__(self, name, current_room, inventory=None):
        self.name = name
        self.current_room = current_room
        self.inventory = [] if inventory == None else inventory

    def set_room(self, room):
        self.current_room = room

    def get_item(self, item):
        inv_item = list(filter(lambda i: i.name == item, self.inventory))
        return inv_item[0] if len(inv_item) else False

    def add_item(self, item):
        self.inventory.append(item)

    def drop_item(self, item):
        self.inventory = list(filter(lambda i: i.name != item, self.inventory))

    def has_light_source(self):
        for item in self.inventory:
            if isinstance(item, LightSource):
                return True
        return False
