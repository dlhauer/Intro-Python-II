# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current_room, inventory=None):
        self.name = name
        self.current_room = current_room
        self.inventory = [] if inventory == None else inventory

    def set_room(self, room):
        self.current_room = room

    def add_item(self, item):
        self.inventory.append(item)
