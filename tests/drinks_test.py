import unittest
from src.room import Room
from src.guest import Guest
from src.song import Song
from src.bar import Bar
from src.drinks import Drinks

class TestDrinks(unittest.TestCase):

    def setUp(self):
        
        self.bar_room1 = Bar()

        self.drink1 = Drinks("Beer", True)
        self.drink2 = Drinks("Tap Water", False)

    def test_if_drink_dict_created(self):
        self.bar_room1.add_drink_to_bar_dict(self.drink1, 5)
        self.assertEqual(1, len(self.bar_room1.drinks_dict))

    def test_access_to_created_drink_data(self):
        self.bar_room1.add_drink_to_bar_dict(self.drink1, 5)

        self.assertEqual(5, self.bar_room1.drinks_dict[self.drink1])

    def test_alchohol_level_of_drink_true(self):
        self.bar_room1.add_drink_to_bar_dict(self.drink1, 5)
        output = self.bar_room1.check_drink_alcohol("Beer")
        self.assertEqual(True, output)

    def test_alchohol_level_of_drink_false(self):
        self.bar_room1.add_drink_to_bar_dict(self.drink2, 1.0)
        output2 = self.bar_room1.check_drink_alcohol("Tap Water")
        self.assertEqual(False, output2)

