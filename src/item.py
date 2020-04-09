class Item:
    def __init__(self, name, description):
        self.name = '-'.join(name.split())
        self.description = description

    def on_take(self):
        print(f'You have picked up the {self.name}!')

    def on_drop(self):
        print(f'You have dropped the {self.name}!')


class LightSource(Item):
    def __init__(self, name, description):
        super().__init__(name, description)

    def on_drop(self):
        print(
            f'Your {self.name} is a light source. It is unwise to drop it.')
