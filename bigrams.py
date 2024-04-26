import nltk

from helpers import get_player_response
import helpers
# Claude Shannon: first reference to n grams

def begin(finished=False):
    helpers.slow_print("You are led down the path through the Woods of Connection.\nThere, you find a man sitting underneath a tree, drinking from a jug.")
    if helpers.get_player_word_count() < 100:
       helpers.slow_print("You are not ready to reflect on your journey yet, please return here when you have explored the other areas in greater detail.")
       response = get_player_response()
       return False
   
    if finished:
        helpers.slow_print("The familiar words of Claushe Dannon echo through your mind \"Remember that the words you say are connected, their meaning will carry you through the rest of your journey\"")
        return True
    

def finish_bigrams():
    print("done")