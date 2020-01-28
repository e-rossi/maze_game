from src.abstract_factory.factories.bombed_maze_factory import BombedFactory
from src.abstract_factory.factories.enchanted_maze_factory import EnchantedFactory
from src.abstract_factory.factories.maze_base_factory import BaseFactory
from src.abstract_factory.gameplay_af import Factory
from src.no_design_pattern.gameplay import BaseGame

if __name__ == '__main__':
    BaseGame.run()
    Factory.run_factory(factory=BaseFactory)
    Factory.run_factory(factory=EnchantedFactory)
    Factory.run_factory(factory=BombedFactory, explode_bomb=True)
