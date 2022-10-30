import unittest
from src.room import Room
from src.guest import Guest
from src.song import Song
from src.bar import Bar
from src.drinks import Drinks

class TestGuest(unittest.TestCase):
    
    def setUp(self):
        
        self.room_1 = Room(1, 10.00)
        self.room_2 = Room(2, 18.00)
        self.room_3 = Room(3, 5.00)

        self.guest1 = Guest("Bob", 18, "Love Story - Taylor Swift", 50.00) 
        self.guest2 = Guest("Billy", 18, "Psycho Killer - Talking Heads", 50.00) 
        self.guest3 = Guest("Bill", 18, "Du Hast - Rammstein", 50.00) 
        self.guest4 = Guest("Abby", 25, "All too well (10 minute edition) - Taylor Swift", 100.00)

    def test_guest_can_pay_room(self):
        self.assertEqual(True, self.guest1.guest_can_pay_room(self.room_1))

    def test_guest_can_buy_alcholic_drink(self):

        self.bar_room1 = Bar()

        self.drink1 = Drinks("Beer", True)
        self.drink2 = Drinks("Tap Water", False)

        self.bar_room1.add_drink_to_bar_dict(self.drink1, 5.00)
        self.bar_room1.add_drink_to_bar_dict(self.drink2, 7.50)
        self.guest1.guest_can_buy_drink(self.drink1, self.bar_room1)
        self.assertEqual(45.00 , self.guest1.guest_wallet)

    def test_guest_can_buy_non_alcholic_drink(self):

        self.bar_room1 = Bar()

        self.drink1 = Drinks("Beer", True)
        self.drink2 = Drinks("Tap Water", False)

        self.bar_room1.add_drink_to_bar_dict(self.drink1, 5.00)
        self.bar_room1.add_drink_to_bar_dict(self.drink2, 7.50)
        self.guest1.guest_can_buy_drink(self.drink2, self.bar_room1)
        self.assertEqual(42.50 , self.guest1.guest_wallet)

    def test_guest_can_add_to_bar_tab(self):

        self.bar_room1 = Bar()

        self.drink1 = Drinks("Beer", True)
        self.drink2 = Drinks("Tap Water", False)

        self.bar_room1.add_drink_to_bar_dict(self.drink1, 5.00)
        self.bar_room1.add_drink_to_bar_dict(self.drink2, 7.50)
        self.guest1.guest_can_buy_drink(self.drink2, self.bar_room1)
        self.assertEqual(7.50 , self.bar_room1.bar_tab)