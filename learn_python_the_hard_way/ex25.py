def break_words(stuff):
    """This function wll break up words for us"""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sort the words"""
    return sorted(words)
def print_first_word(words):
    """Print first word"""
    word = words.pop[0]
    print(word)
def print_last_word(words):
    """Print last word"""
    word = words.pop[-1]
def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words"""
    words = break_words(sentence)
    return sort_words(words)
def print_first_and_last(sentence):
    """Print first and last word of the sentence"""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)
def print_first_and_last_sorted(sentence):
    words = sort_sentence()
    print_last_word(words)
    print_last_word(words)




#in terminal cmd
#>>python
#>>import ex25
#>>sentence = "xdxd xd xd xd xd xd xddd"
#>>words = ex25.break_words(sentence)
#>>words

