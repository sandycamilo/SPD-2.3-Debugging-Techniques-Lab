# By Kami Bigdely
# Decompose conditional: You have a complicated conditional(if-then-else) statement. Extract
# methods from the condition, then part, and else part(s).

def make_alert_sound():
    print('made alert sound.')
    
def make_accept_sound():
    print('made acceptance sound')

def check_for_toxin():
    for ingredient in ingredients:
        if ingredient in toxins:
            print('!!!')
            print('there is a toxin in the food!')    
            print('!!!')
            return make_alert_sound()
        else: 
            print('***')
            print('Toxin Free')
            print('***')
            return make_accept_sound()

ingredients = ['sodium benzoate']
toxins = ['sodium nitrate', 'sodium benzoate', 'sodium oxide']
check_for_toxin()