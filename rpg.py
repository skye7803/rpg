

class Inventory:
    def __init__(self):
        self.sword = False

class Begin:
    def __init__(self, inv):
        self.command = ''
        self.inventory = inv

    def WakeUp(self):
        print("You wake up in the woods, unable to discern your location or who you are. ")
        print("You can't even remember your own name.")
        print("You see a nearby village.")
        self.command = input("Head towards it? ")
        self.HeadTowardsTown()

    def HeadTowardsTown(self):
        if self.command in ['yes', 'y']:
            print("As you approach the village, there becomes apparent a road. ")
            print("You get on the road on start heading towards the village again. ")
            print("As you get near the town, more and more people start passing you.")
            self.command = input("Try to talk to one of them? ")
            self.TalkToPerson()
        else:
            print("You sit and do nothing")
            print("Then you die")
            main.GameOver()

    def TalkToPerson(self):
        if self.command in ['yes', 'y']:
            print('You walk up to a friendly old man')
            print('"Ah, Young one, you come from a far away land, and have a long journey ahead of you," He says.')
            print('"Please, Accept this gift to aid your journey,". He gives you a small worn sword')
            print('You then decide to head towards the village once again')
            inventory.sword = True
            main.Village()
        else:
            print('You decide not to talk to anyone and instead to head straight to the village.')
            main.Village()

    def Question(self):
        main.loop = True
        while main.loop:
            self.command = input('What would you like to ask next? ')
            if self.command in ['who am i?']:
                main.loop = False
                print('"Well, That\'s for you to find out" said the bartender')
                print('"I can aid you in your quest of self discovery, however," He said.')
            elif self.command in ['who are you?']:
                main.loop = False
                print('"Me? I\'m just the bartender," He stated ominously.')
                print('"I do offer quests however," He said.')
            elif self.command in ['what is this sword?']:
                main.loop = False
                print('"Hmm, not sure." He stated.')
                print('"It looks as though it may be useful for these tasks however," He said.')
            else:
                print('"Didn\'nt quite catch that"')
            main.Tavern()

class Main:
    def __init__(self, inv):
        self.command = ''
        self.helplist = ['']
        self.firsttime = True
        self.loop = True
        self.questlist = ['Wanted, runaway bandit.', 'Help, missing person']
        self.inventory = inv

    def GameOver(self):
        print("  ____                         ___                 ")
        print(" / ___| __ _ _ __ ___   ___   / _ \__   _____ _ __ ")
        print("| |  _ / _` | '_ ` _ \ / _ \ | | | \ \ / / _ \ '__|")
        print("| |_| | (_| | | | | | |  __/ | |_| |\ V /  __/ |   ")
        print(" \____|\__,_|_| |_| |_|\___|  \___/  \_/ \___|_|  ")

    def Village(self):
        while self.loop:
            print('You walk into the village and marvel at the amount of people')
            print('Armor shop')
            print('Weapon shop')
            print('Inn')
            print('Tavern')
            print('Magic Shop')
            self.command = input('Where do you want to go? ')
            if self.command in ['armor shop', 'as']:
                print('Armor shop\'s closed')
            elif self.command in ['weapon shop', 'ws']:
                print('Weapon shop\'s closed')
            elif self.command in ['inn', 'i']:
                print('Inn\'s closed')
            elif self.command in ['magic shop', 'ms']:
                print('Magic shop\'s closed')
            elif self.command in ['tavern', 't']:
                self.loop = False
                if self.firsttime:
                    print('You walk into a warm, welcoming tavern with a bartender and a few regulars.')
                    print('You walk up to the bartender and start some chit chat')
                    print('He reveals you\'re in a town called Ravel in the province of Fradin.')
                    if inventory.sword:
                        self.helplist = ['"who am i?"', '"who are you?"', '"what is this sword?"']
                    else:
                        self.helplist = ['"who am i?"', '"who are you?"']
                    print(self.helplist)
                    begin.Question()
                    self.firsttime = False
                else:
                    self.Tavern()

    def Tavern(self):
        print('"Here are the tasks I have available for you."')
        print(self.questlist)


begin = Begin()

main = Main()

inventory = Inventory()

begin.WakeUp()

main = Main(inventory)

begin.WakeUp()
