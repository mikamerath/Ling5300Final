import re

import bigrams
import fsa_ruins
import helpers

from helpers import get_player_response, slow_print

def main():
    welcome()
    slow_print(helpers.player_name + ", you begin your journey in the village of Santosan")
    # fsa_ruins.begin()
    bigrams.begin()
    slow_print("Wow! You won! You are a massive deal " + helpers.player_name + "!")
    return


def welcome():
    helpers.player_name = get_player_response("Welcome adventurer! What is your name? ")
    helpers.text_speed_name = get_player_response("How fast would you like the text to be displayed currently set to medium? (slow, medium, fast, instant)")
    helpers.set_text_speed(helpers.text_speed_name)


if __name__ == "__main__":
    main()
