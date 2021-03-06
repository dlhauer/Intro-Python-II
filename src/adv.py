from room import Room
from player import Player
from item import Item
from item import LightSource
from action import Action
from textwrap import wrap

mappy = Item('map', 'A dusty map. Only the faintest detail is discernible.')
suit = Item('suit of armor', 'An old suit of iron. But where is its owner?')
candelabra = LightSource(
    'candelabra', 'The candles are still lit. But who lit them?')
quill_and_ink = Item(
    'quill and ink', 'A worn quill tip. Enough ink only to make a few essential notes.')
parchment = Item(
    'parchment', 'Weathered and old, yet its surface is perfectly clean.')
rope = Item('rope', 'Rough to the touch. Forty fathoms in length')
sword = Item(
    'sword', 'An exceedingly well–cared-for blade. A bronze snake coiled around the hilt.')
keys = Item('rusty keys',
            'A ring of five keys. So worn and rusted, would they fit in a lock any more?')
envelope = Item('wax sealed envelope',
                'A yellowed envelope sealed with wax. Do you dare open it?')
compass = Item('compass', 'Find North, the only truth that remains certain.')
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons.", [mappy, suit]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [candelabra, quill_and_ink, parchment]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [rope]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [sword, keys, envelope], False),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [compass], False),
}

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

player = Player('Daaaaaaaaan', room['outside'])
directions = [
    Action('n', 'move north'),
    Action('s', 'move south'),
    Action('e', 'move east'),
    Action('w', 'move west')
]
accepted_actions = directions.copy()
accepted_actions.extend([
    Action('i', 'print inventory'),
    Action('take [item]', 'add [item] to your inventory'),
    Action('drop [item]', 'leave [item] in current room'),
    Action('q', 'quit')
])
while True:
    has_light = (player.has_light_source()
                 or player.current_room.has_light_source()
                 or player.current_room.is_light)
    if has_light:
        print(
            f'\nCurrent room: {player.current_room.name}.\n'
            f'{player.current_room.description}\n\n'
            'Available items:'
        )
        for item in player.current_room.items:
            text = wrap(f'{item.name}: {item.description}', 60)
            for line in text:
                print(line)
    else:
        print("It's pitch black in here!")
    choices = '\n'.join(
        list(map(lambda action: f'{action.key} - {action.value}', accepted_actions)))
    player_input = input(f'\nWhat would you like to do?\n{choices}\n').split()
    print('\n')
    action = player_input[0]
    if len(player_input) == 2:
        item = player_input[1]
    if action not in list(map(lambda action: action.key.split()[0], accepted_actions)):
        print('\nWhoa, try that again. Make sure you enter a valid command.')
    elif action == 'q':
        text = wrap('I never thought you were cut out for this adventure, anyway. '
                    f'Have a nice life, {player.name}, you big quitter.', 60)
        for line in text:
            print(line)
        print('\n')
        break
    elif action in list(map(lambda action: action.key, directions)):
        next_room = getattr(player.current_room, f'{action}_to')
        if next_room:
            player.set_room(next_room)
        else:
            print('Oops! There is nothing in that direction. Try again.')
    elif action == 'take':
        room_item = player.current_room.get_item(item)
        if room_item and has_light:
            player.add_item(room_item)
            player.current_room.remove_item(item)
            room_item.on_take()
        elif room_item and not has_light:
            print('LOL, good luck picking that up in the dark.')
        else:
            print(f"Say what? There's no {item} in here.")
    elif action == 'drop':
        inv_item = player.get_item(item)
        if inv_item:
            player.drop_item(item)
            player.current_room.add_item(inv_item)
            inv_item.on_drop()
        else:
            print(f"Huh? You don't even have {item}.")
    elif action == 'i':
        if len(player.inventory):
            print('Your inventory:\n')
            for item in player.inventory:
                print(item.name)
        else:
            print("You don't have any inventory yet!")
