import re

import helpers
import bigrams

from helpers import get_player_response, slow_print

def main():
    welcome()
    slow_print(helpers.player_name + ", you begin your journey in the village of Santosan")
    slow_print("Wow! You won! You are a massive deal " + helpers.player_name + "!")
    bigrams.begin()
    return


def welcome():
    helpers.player_name = input("Welcome adventurer! What is your name? ")
    helpers.text_speed_name = get_player_response("How fast would you like the text to be displayed currently set to medium? (slow, medium, fast)")
    helpers.set_text_speed(helpers.text_speed_name)


if __name__ == "__main__":
    main()
