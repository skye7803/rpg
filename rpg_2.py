class Loop:
    def __init__(self, loc):
        self.loop = True
        self.location = loc

    def mainLoop(self):
        while self.loop:
            print('You are ' + self.location.areas[self.location.currentArea]['text'])
            self.command = input('Which direction would you like to head? ')
            if self.command in ['north', 'n']:
                if 'north' in self.location.areas[self.location.currentArea]:
                    self.location.currentArea = self.location.areas[self.location.currentArea]['north']
                elif 'north//' in self.location.areas[self.location.currentArea]:
                    print('You cannot go that way because of a ' + self.location.areas[self.location.currentArea]['north//'])
                else:
                    print('You found a bug!')
            if self.command in ['east', 'e']:
                if 'east' in self.location.areas[self.location.currentArea]:
                    self.location.currentArea = self.location.areas[self.location.currentArea]['east']
                elif 'east//' in self.location.areas[self.location.currentArea]:
                    print('You cannot go that way because of a ' + self.location.areas[self.location.currentArea]['east//'])
                else:
                    print('You found a bug!')
            if self.command in ['south', 's']:
                if 'south' in self.location.areas[self.location.currentArea]:
                    self.location.currentArea = self.location.areas[self.location.currentArea]['south']
                elif 'south//' in self.location.areas[self.location.currentArea]:
                    print('You cannot go that way because of a ' + self.location.areas[self.location.currentArea]['south//'])
                else:
                    print('You found a bug!')
            if self.command in ['west', 'w']:
                if 'west' in self.location.areas[self.location.currentArea]:
                    self.location.currentArea = self.location.areas[self.location.currentArea]['west']
                elif 'west//' in self.location.areas[self.location.currentArea]:
                    print('You cannot go that way because of a ' + self.location.areas[self.location.currentArea]['west//'])
                else:
                    print('You found a bug!')




class Location:
    def __init__(self):
        self.currentArea = 'dungeon'
        self.areas = {
            'dungeon': {
                'id': 'dungeon',
                'text': 'in a dungeon',
                'north//': 'a wall',
                'east//': 'a wall',
                'south//': 'a wall',
                'west//': 'a door',
            },
        }


location = Location()

loop = Loop(location)

loop.mainLoop()
