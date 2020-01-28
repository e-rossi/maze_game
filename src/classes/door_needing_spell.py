from src.classes.door import Door
from src.classes.spell import Spell


class DoorNeedingSpell(Door):
    def __init__(self, r1, r2):
        super(DoorNeedingSpell, self).__init__(r1, r2)
        self.spell = Spell()

    def enter(self):
        print('  + This door needs a spell...', self.spell)
        if self.isOpen:
            print('You have passed through the door')
        else:
            print('This door needs to be opened before you pass through it...')
