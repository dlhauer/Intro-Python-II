class Item:
    def __init__(self, name, description):
        self.name = '-'.join(name.split())
        self.description = description

    def on_take(self):
        print(f'You have picked up the {self.name}!')

    def on_drop(self):
        print(f'You have dropped the {self.name}!')
