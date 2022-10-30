import unittest
from src.room import Room
from src.guest import Guest

class TestRoom(unittest.TestCase):
    
    def setUp(self):
        
        self.room_1 = Room(1, 10.00)
        self.room_2 = Room(2, 18.00)
        self.room_3 = Room(3, 5.00)

        self.guest1 = Guest("Adam", 27, "Love Story - Taylor Swift", 50.00) 
        self.guest2 = Guest("Rory", 26, "Psycho Killer - Talking Heads", 50.00) 
        self.guest3 = Guest("Claire", 17, "Du Hast - Rammstein", 50.00) 
        self.guest4 = Guest("Abby", 26, "All too well (10 minute edition) - Taylor Swift", 5.00)

    def test_room_has_capacity(self):
        self.assertEqual(2,self.room_2.capacity)

    def test_room_has_entry_fee(self):
        self.assertEqual(10.00, self.room_1.entry_fee)

    def test_room_is_empty(self):
        self.assertEqual(0, len(self.room_1.room_occupants))

    def test_room_has_space(self):
        result = self.room_1.check_room_has_space()
        self.assertEqual(True, result)


    def test_room_add_guest(self):
        self.room_2.guest_check_in(self.guest1, self.room_2)
        self.room_2.guest_check_in(self.guest2, self.room_2)    
        # print(self.room_2.room_occupants)    
        self.assertEqual(2, len(self.room_2.room_occupants))


    def test_room_add_guest_conditional_has_paid(self):
        self.room_1.guest_check_in(self.guest1, self.room_1)
        self.assertEqual(True, self.room_1.room_fee_paid)

    def test_room_add_guest_conditional_cannot_pay(self):
        self.room_1.guest_check_in(self.guest4, self.room_1)
        self.assertEqual(False, self.room_1.room_fee_paid)
        self.assertEqual(0, len(self.room_1.room_occupants))

    def test_room_add_guest_conditional_room_full(self):
        self.room_1.guest_check_in(self.guest1, self.room_1)
        self.room_1.guest_check_in(self.guest2, self.room_1)
        self.assertEqual(1, len(self.room_1.room_occupants))


    def test_room_checkout_guest(self):

        self.room_2.guest_check_in(self.guest1, self.room_2)
        self.room_2.guest_check_in(self.guest2, self.room_2)
        self.assertEqual(2, len(self.room_2.room_occupants))
        self.room_2.guest_check_out()
        self.assertEqual(0, len(self.room_2.room_occupants))


        
