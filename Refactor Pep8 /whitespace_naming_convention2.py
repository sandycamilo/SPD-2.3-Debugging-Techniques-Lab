# By Kami Bigdely
# PEP8 - whitespaces and variable names.

class Pizza:
    def __init__ (self, bread_type, cheese_type, meat_type, 
                  toppings, size):
        self.bread_type= bread_type
        self.cheese_type = cheese_type
        self.meat_type= meat_type
        self.toppings = toppings
        self.size = size  

    @classmethod
    def create_chicago_pizza (chicago_pizza, size):
        bread = 'deep-dish bread'
        cheese = 'mozzarella cheese'
        meat= 'italian sausage'
        toppings = ['green bell pepper','mushroom', 
                    'chunky tomato sauce', 'onion']
        return chicago_pizza(bread, cheese, meat, toppings, size) 

    @classmethod
    def create_california_pizza(cali_pizza, meat_type, size):
        bread = 'thin crust'
        cheese = 'feta cheese'
        toppings = ['garlic', 'spinach', 'broccoli', 'olives', 
                    'red onion', 'red bell pepper']
        return cali_pizza(bread, cheese, meat_type, toppings, size) 

    def print_info(self):
        print('Bread type is: ', self.bread_type)
        print('Cheese type is: ', self.cheese_type)
        print('Meat type is: ', self.meat_type)
        print('Toppings are: ', end='')
        print(', '.join(map(str, self.toppings)))

pizza = Pizza.create_california_pizza('chicken', 'large')
pizza.print_info()