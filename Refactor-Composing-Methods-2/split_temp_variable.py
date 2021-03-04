# by Kami Bigdely
# Split temporary variable

def get_sandwhich_weight():
    weight = 2 * patty + 4 * pickle + 3 * tomatoes + 2 * buns
    return weight

def ny_burger(weight):
    return weight + 2 * lettuce

def seoul_burger(weight):
    return weight + kimchi + mayo + golden_fried_onion

if __name__ == "__main__": 
    patty = 70 # [gr]
    pickle = 20 # [gr]
    tomatoes = 25 # [gr]
    lettuce = 15 # [gr]
    buns = 95 # [gr]
    kimchi = 30 # [gr]
    mayo = 5 # [gr]
    golden_fried_onion = 20 # [gr]

    get_sandwhich_weight()
    ny_weight = ny_burger(get_sandwhich_weight())
    seoul_weight = seoul_burger(get_sandwhich_weight())
    print("NY Burger Weight", ny_weight)
    print("Seoul Kimchi Burger Weight", seoul_weight)