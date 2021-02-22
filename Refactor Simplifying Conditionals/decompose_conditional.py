# By Kami Bigdely
# Decompose conditional: You have a complicated conditional(if-then-else) statement. Extract
# methods from the condition, then part, and else part(s).

ingredients = ['sodium benzoate']
toxins = ['sodium nitrate', 'sodium benzoate', 'sodium oxide']

def make_alert_sound():
    print('made alert sound.')
    
def make_accept_sound():
    print('made acceptance sound')

def no_toxin():
    print('***')
    print('Toxin Free')
    print('***')
    return make_accept_sound()

def toxin_present():
    print('!!!')
    print('there is a toxin in the food!')    
    print('!!!')
    return make_alert_sound()

def check_for_toxin():
    for ingredient in ingredients:
        if ingredient in toxins:
            return toxin_present()
        else: 
            return no_toxin()

check_for_toxin()