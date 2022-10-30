import unittest
from src.room import Room
from src.guest import Guest
from src.song import Song
from src.bar import Bar
from src.drinks import Drinks

class TestBar(unittest.TestCase):
    def setUp(self):

        
        self.bar_room1 = Bar()
        
        self.drink1 = Drinks("Beer", True)
        self.drink2 = Drinks("Tap Water", False)

        self.guest1 = Guest("Bob", 17, "Love Story - Taylor Swift", 50.00) 
        self.guest2 = Guest("Billy", 18, "Psycho Killer - Talking Heads", 50.00) 
        self.guest3 = Guest("Bill", 18, "Du Hast - Rammstein", 50.00) 
        self.guest4 = Guest("Abby", 25, "All too well (10 minute edition) - Taylor Swift", 100.00)




    def test_output_of_bar_to_add_tab(self):

        self.bar_room1.add_drink_to_bar_dict(self.drink1, 5)

        self.bar_room1.bar_to_add_to_tab(self.drink1)
        self.assertEqual(5 , self.bar_room1.bar_tab)

