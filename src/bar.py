class Bar:
    def __init__(self):
        self.drinks_dict = {}
        self.bar_tab = 0.00


    def check_drink_alcohol(self, drink_to_check):
        for drink in self.drinks_dict:
            if drink.drink_name == drink_to_check:
                return drink.drink_alcoholic

    def return_drink_price(self, drink_instance):
        output = self.drinks_dict[drink_instance]
        return output

    def add_drink_to_bar_dict(self, drink, drink_price):
        if drink not in self.drinks_dict:
            self.drinks_dict[drink] = drink_price

    def bar_to_add_to_tab(self, drink_instance):
        self.bar_tab += self.drinks_dict[drink_instance]

    # def check_guest_age(self, guest_instance):
    #     if guest_instance.guest_age >= 18:
    #         return True
    #     return False


