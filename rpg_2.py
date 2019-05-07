class Loop:
    def __init__(self, loc, inv):
        self.loop = True
        self.location = loc
        self.inventory = inv
        self.move_command = ''

    def gameOver(self):
        print('  ____                         ___  ')
        print(' / ___| __ _ _ __ ___   ___   / _ \__   _____ _ __ ')
        print('| |  _ / _` | `_ ` _ \ / _ \ | | | \ \ / / _ \  __|')
        print('| |_| | (_| | | | | | |  __/ | |_| |\ V /  __/ |  ')
        print(' \____|\__,_|_| |_| |_|\___|  \___/  \_/ \___|_| ')

    def mainLoop(self):
        while self.loop:
            print('You are ' + self.location.areas[self.location.currentArea]['text'])
            self.move_command = input('Which direction would you like to go? ')
            self.move('north', 'n', 'north//')
            self.move('east', 'e', 'east//')
            self.move('south', 's', 'south//')
            self.move('west', 'w', 'west//')
            if self.inventory.hunger > 0:
                self.inventory.hunger -= 1
            if self.inventory.hunger == 3:
                print('Getting hungry...')
            if self.inventory.hunger == 0:
                self.inventory.health -= 1
                print('Starving!')
            if self.inventory.health == 0:
                self.gameOver()


    def move(self, direction, letter, false_direction):
        if self.move_command in [direction, letter]:
            if direction in self.location.areas[self.location.currentArea]:
                self.location.currentArea = self.location.areas[self.location.currentArea][direction]
            elif false_direction in self.location.areas[self.location.currentArea]:
                print(
                    'You cannot go that way because of a ' +
                    self.location.areas[self.location.currentArea][false_direction])
            else:
                print('You found a bug!')


class Inventory:
    def __init__(self):
        self.health = 10
        self.hunger = 10
        self.contents = {

        }


class Location:
    def __init__(self):
        self.currentArea = 'starting_dungeon'
        self.areas = {
            'starting_dungeon': {
                'text': 'in a damp dungeon',
                'north//': 'a wall',
                'east//': 'a wall',
                'south//': 'a wall',
                'west': 'starting_hallway',
            },
            'starting_hallway': {
                'text': 'in a poorly lit hallway',
                'north': 'starting_stairs',
                'east': 'starting_dungeon',
                'south//': 'a wall',
                'west//': 'a wall',

            },
            'starting_stairs': {
                'text': 'in a crumbling staircase',
                'north': 'starting_outside',
                'east//': 'a wall',
                'south//': 'starting_hallway',
                'west//': 'a wall',
            },
        }


location = Location()

inventory = Inventory()

loop = Loop(location, inventory)

loop.mainLoop()
