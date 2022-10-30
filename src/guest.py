
class Guest:
    
    def __init__(self, guest_name, guest_age, fav_song, guest_wallet):
        self.guest_name = guest_name
        self.guest_age = guest_age
        self.fav_song = fav_song
        self.guest_wallet = guest_wallet

    def guest_can_pay_room(self, room_choice):
        if self.guest_wallet >= room_choice.entry_fee:
            return True
        return False

    def check_song_in_playlist(self, song, playlist):
        if song in playlist.song_list:
            return True
        return False      

    def add_song_to_list(self, song, playlist):
        if not self.check_song_in_playlist(song, playlist):
            playlist.song_list.append(song)

    def guest_fav_song_in_playlist(self, playlist, guest_to_check):
        for song in playlist.song_list:
            if guest_to_check.fav_song == song:
                return "Whoo!"

    def guest_has_cash(self, drink_instance, bar_instance):
        if self.guest_wallet >= bar_instance.return_drink_price(drink_instance):
            return True
        return False


    

    def guest_can_buy_drink(self, drink_instance, bar_instance):
        if self.guest_has_cash(drink_instance, bar_instance) and bar_instance.check_drink_alcohol(drink_instance.drink_name):
            if self.guest_age >= 18:
                self.guest_wallet -= bar_instance.return_drink_price(drink_instance)
                bar_instance.bar_to_add_to_tab(drink_instance)

        elif self.guest_has_cash(drink_instance, bar_instance) and not bar_instance.check_drink_alcohol(drink_instance.drink_name):
            self.guest_wallet -= bar_instance.return_drink_price(drink_instance)
            bar_instance.bar_to_add_to_tab(drink_instance)

    # def guest_can_buy_drink(self, drink_instance, bar_instance, guest_instance):
    #     if bar_instance.check_drink_alcohol(drink_instance.drink_name) == False:
    #         if self.guest_has_cash(drink_instance, bar_instance):
    #             guest_instance.guest_wallet - bar_instance.return_drink_price(drink_instance)
    #             bar_instance.bar_to_add_to_tab(drink_instance)
    #     elif bar_instance.check_drink_alcohol(drink_instance.drink_name):
    #         if self.guest_has_cash(drink_instance, bar_instance) and bar_instance.check_guest_age(guest_instance):
    #             drink_cost = bar_instance.return_drink_price(drink_instance)
    #             guest_instance.guest_wallet - drink_cost
    #             bar_instance.bar_to_add_to_tab(drink_instance)

            






        # if wallet >= drink_dict[drink_to_buy]:
        #     if bar_instance.check_drink_alcohol(drink_to_buy.drink_name) == False:
        #         guest_instance.guest_wallet -= drink_dict[drink_to_buy]
        #         bar_instance.bar_to_add_to_tab(drink_to_buy)
        #     elif bar_instance.check_drink_alcohol(drink_to_buy.drink_name) == True:
        #         if bar_instance.check_guest_age(guest_instance):
        #             guest_instance.guest_wallet -= drink_dict[drink_to_buy]
        #             bar_instance.bar_to_add_to_tab(drink_to_buy)


