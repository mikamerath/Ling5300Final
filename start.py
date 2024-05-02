import re

import bigrams
import fsa_ruins
import grammar_mountains
import helpers
import old_woman

from helpers import get_player_response, slow_print

def main():
    welcome()
    village_loop()
    slow_print("Wow! You won! You are a massive deal " + helpers.player_name + "!")
    return



def welcome():
    helpers.player_name = get_player_response("Welcome adventurer! What is your name? ")
    helpers.text_speed_name = get_player_response("How fast would you like the text to be displayed? (slow, medium, fast, instant) The current setting is medium.")
    helpers.set_text_speed(helpers.text_speed_name)
    slow_print(helpers.player_name + ", you begin your journey in the village of Santosan, a small town" +
               "\nnestled in between several distinct landmarks. The Grammar Mountains are to the North," +
               "\nthe FSA Ruins to the East, and the Forest of Connection to the South. As you wake" +
               "\nup this Summer morning, you are greeted with a letter from the Village Elder." +
               "\nShe asks that you to meet her at her dwelling as soon as you are able.")

def village_loop():
    # fsa_ruins.begin()
    # bigrams.begin()
    # grammar_mountains.begin()
    while True:
        result = False
        response = get_player_response("You are now in the Village of Santosan. Where would you like to go?")
        if re.match(r"[\w\s]*(?:[Nn]orth|[Gg]rammar|[Mm]ountain)[\w\s]*", response):
            slow_print("You head North towards the Grammar Mountains.")
            grammar_mountains.begin()
        elif re.match(r"[\w\s]*(?:[Ff]sa|FSA|[Rr]uins|[Ee]ast)[\w\s]*", response):
            slow_print("You head East towards the FSA ruins.")
            fsa_ruins.begin()
        elif re.match(r"[\w\s]*(?:[Ff]orest|[Cc]onnection|[Ss]outh)[\w\s]*", response):
            slow_print("You head South towards the Forest of Connection.")
            bigrams.begin()
        elif re.match(r"[\w\s]*(?:[Tt]own|[Oo]ld|[Ll]ady|[Ww]oman|[Hh]ouse|[Vv]illage|[Ee]lder)[\w\s]*", response):
            slow_print("You head towards the old lady's house.")
            result = old_woman.begin()
        else:
            slow_print("Confused, you wander around the village aimlessly.")
        
        if result:
            break
    end()

def end():
    slow_print("So ends the story of " + helpers.player_name + "... for now.")

if __name__ == "__main__":
    main()
