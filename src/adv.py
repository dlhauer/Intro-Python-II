from room import Room
from player import Player

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons."),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
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
directions = ['n', 's', 'e', 'w']
accepted_actions = directions.copy()
accepted_actions.append('q')
while True:
    print(
        f'\nCurrent room: {player.current_room.name}.\n'
        f'{player.current_room.description}\n'
    )
    action = input("""What would you like to do?\n
    n - move north\n
    s - move south\n
    e - move east\n
    w - move west\n
    q - quit\n""")
    if action not in accepted_actions:
        print('\nWhoa, try that again. Make sure you enter a valid command.')
    elif action == 'q':
        print('\nI never thought you were cut out for this adventure, anyway. '
              f'Have a nice life, {player.name}, you big quitter.\n'
              )
        break
    else:
        next_room = getattr(player.current_room, f'{action}_to')
        if next_room:
            player.set_room(next_room)
        else:
            print('\nOops! There is nothing in that direction. Try again.')
