class Item:
    def __init__(self, name, description):
        self.name = '-'.join(name.split())
        self.description = description
