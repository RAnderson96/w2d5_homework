

class Room:
    def __init__(self, capacity, entry_fee):
        self.capacity = capacity
        self.entry_fee = entry_fee
        self.room_songs = []
        self.room_occupants = []
        self.room_fee_paid = False

    def check_room_has_space(self):
        return len(self.room_occupants) < self.capacity

    def guest_check_in(self, guest_to_add, room_choice):
        if guest_to_add.guest_can_pay_room(room_choice) and self.check_room_has_space():

            self.room_occupants.append(guest_to_add.guest_name)
            self.room_fee_paid = True

    def guest_check_out(self):
        self.room_occupants.clear()
