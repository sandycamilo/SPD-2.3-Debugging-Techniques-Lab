# by Kami Bigdely
# Extract Class

class Food: 
    def __init__(self, food):
        self.food = food
    
    def food_name(self, key):
        print("Name:",key)
    
    def prep_time(self):
        print("Prep time:",value[0], "mins")
    
    def is_it_veggie(self):
        print("Is Veggie?", 'Yes' if value[1] else "No")
    
    def define_food_type(self):
        print("Food Type:", value[2])
    
    def define_cuisine(self):
        print("Cuisine:", value[3])
    
    def ingredients(self):   
        for item in value[4]:
            print(item, end=', ')
    
    def recipe(self):
        print("recipe", value[5])
        print("***")

if __name__ == "__main__":
    foods = {'butternut squash soup':[45, True, 'soup','North African',\
        ['butter squash','onion','carrot', 'garlic','butter','black pepper', 'cinnamon','coconut milk']\
            ,'1. Grill the butter squash, onion, carrot and garlic in the oven until'
            'they get soft and golden on top 2. Put all in blender with'
            'butter and coconut milk. Blend them till they become puree. Then move the content into a pot'
                '. Add coconut milk. Simmer for 5 mintues.'],
            'shirazi salad':[5, True, 'salad','Iranian', ['cucumber', 'tomato', 'onion', 'lemon juice'], \
                '1. dice cucumbers, tomatoes and onions 2. put all into a bowl 3. pour lemon juice 3. add salt'
                    '4. Mixed them thoroughly'],
            'Home-made Beef Sausage': [60, False, 'deli','All',['sausage casing', 'regular ground beef','garlic',\
                'corriander seeds','black pepper seeds','fennel seed','paprika'],'1. In a blender,'
                    ' blend corriander seeds, black pepper seeds, fennel seeds and garlic to make'
                    'the seasonings 2. In a bowl, mix ground beef with the'
                    'seasoning 3. Add all the content to a sausage stuffer. Put the casing on'
                    "the stuffer funnel. Rotate the stuffer's handle (or turn it on) to make your yummy sausages!"]}

    foods = Food(foods)
    for key, value in foods.food.items():
        foods.food_name(key)
        foods.prep_time()
        foods.is_it_veggie()
        foods.define_food_type()
        foods.define_cuisine()
        foods.ingredients()
        foods.recipe()