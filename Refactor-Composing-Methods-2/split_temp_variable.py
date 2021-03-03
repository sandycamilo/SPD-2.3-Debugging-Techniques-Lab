# by Kami Bigdely
# Split temporary variable

class Burger:
    PATTY = 70 # [gr]
    PICKLE = 20 # [gr]
    TOMATO = 25 # [gr]
    LETTUCE = 15 # [gr]
    BUN = 95 # [gr]

    def __init__(self, name):
        self.name = name

    def calc_reg_weight(self):
        return 2 * self.PATTY + 4 * self.PICKLE + 3 * self.TOMATO + 2 \
                                        * self.LETTUCE + 2 * self.BUN

    def get_total_weight(self):
        print(f'{self.name}: {self.calc_reg_weight()} grams')

class SeoulBurger(Burger):
    KIMCHI = 30 # [gr]
    MAYO = 5 # [gr]
    GOLDEN_FRIED_ONION = 20 # [gr]

    def __init__(self, name):
        super().__init__(name)

    def calc_seoul_weight(self):
        return super().calc_reg_weight() + self.KIMCHI + self.MAYO + \
                                                self.GOLDEN_FRIED_ONION

Burger('NY Burger').get_total_weight()
SeoulBurger('Seoul Kimchi Burger').get_total_weight()