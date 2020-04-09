# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description, items=None):
        self.name = name
        self.description = description
        self.n_to = ''
        self.s_to = ''
        self.e_to = ''
        self.w_to = ''
        self.items = [] if items == None else items

    def remove_item(self, item):
        self.items = list(filter(lambda i: i.name != item, self.items))

    def add_item(self, item):
        self.items.append(item)
