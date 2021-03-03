# by Kami Bigdely
# Rename Method
# Reference: https://parade.com/1039985/marynliles/pick-up-lines/

def calculate_area_unde_graph(graph): 
    """Calculate the area under the input graph."""
    # bla bla bla.
    pass

#####################
def get_max_value(li):
    m = li[0]
    for value in li:
        if value > m:
            m = value
    return m

############################
def convert_to_words_list(sentence):  
    words = sentence[0:].split(' ')
    return words

if __name__ == "__main__":
    li = [5, -1, 43, 32, 87, -100]
    print(get_max_value(li))
    print(convert_to_words_list('If you were a vegetable, \
                                 you’d be a ‘cute-cumber.'))
