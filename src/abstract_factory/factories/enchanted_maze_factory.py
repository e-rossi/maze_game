from src.abstract_factory.factories.maze_base_factory import BaseFactory
from src.classes.door_needing_spell import DoorNeedingSpell
from src.classes.enchanted_room import EnchantedRoom
from src.classes.spell import Spell


class EnchantedFactory(BaseFactory):
    @classmethod
    def make_room(cls, n):
        return EnchantedRoom(n, cls.cast_spell())

    @classmethod
    def make_door(cls, r1, r2):
        return DoorNeedingSpell(r1, r2)

    @classmethod
    def cast_spell(cls):
        return Spell().name
