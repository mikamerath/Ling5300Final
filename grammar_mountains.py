import re

import helpers

from helpers import slow_print, get_player_response
from cky import is_sentence

# Noam Chomsky
PASS_PHRASE_NUM = 2

def begin():
    if helpers.results[PASS_PHRASE_NUM]:
        slow_print("You return to the Grammar Mountains satisfied upon seeing the labors of your work" +
                   "\nLooking around, you do not see anything interesting in the area and decide to return to Santosan.")
        return True
    
    response = get_player_response("As you reach the base of the mountains, you notice" +
                                   "\nthat there is a trail that leads up to the top. What do you do?")
    
    while True:
        if re.match(r"[\w\s]*(?:[Ll]eave|[Rr]eturn|[Ss]antosan|[Gg]ive up|[Ee]xit)[\w\s]*", response):
            slow_print("Unsure of what to do, you head back to the village of Santosan")
            return False
        elif re.match(r"[\w\s]*(?:[Ii]nvestigate|[Ll]ook around|[Hh]ike|[Gg]o up|[Pp]eak|[Ff]urther|[Ss]earch|[Dd]elve|[Ee]xamine|[Ee]xplore|[Ii]nspect|[Tt]rail|[Ff]ollow|[Hh]ead)[\w\s]*", response):
            slow_print("You begin to head up the trail towards the peak of the mountain." +
                   "\nThe journey is long and arduous, but after 30 minutes, you arrive at the top.")
            return puzzle()
        else:
            slow_print("Confused, you " + response)
            response = get_player_response("After some time, you stop, the trail to the top of the mountain" + 
                                           "\nstill in your sights. What would you like to do now?")

def puzzle():
    slow_print("At the peak of the mountain, you see a tablet on a stone table with the following inscriptions: " +
               "\n\tS -> NP VP" +
               "\n\tNP -> Det N | NP PP" +
               "\n\tVP -> V NP | V PP" +
               "\n\tPP -> P NP" + 
               "\n\tDet -> a | the" +
               "\n\tN -> thing | person | hill | man | woman" + 
               "\n\tV -> walked | saw | ate" +
               "\n\tP -> up | on | in")

    slow_print("As you study the inscriptions, a console pops out.")
    while True:
        response = get_player_response("On the screen is printed, \"Please provide me with a sentence that is part of the grammar.\"")
        if re.match(r"[\w\s]*(?:[Ll]eave|[Rr]eturn|[Ss]antosan|[Gg]ive up|[Ee]xit)[\w\s]*", response):
            slow_print("Unsure of what to do, you head back to the village of Santosan")
            return False
        elif is_sentence(response):
            slow_print("\"That is correct!\" The machine prints. Here is a clue to guide you on your journey: " +
                       "\"" + helpers.pass_phrases[PASS_PHRASE_NUM] + "\"")
            helpers.add_pass_phrase_to_player(PASS_PHRASE_NUM)
            slow_print("With a skip in your step, you head down the mountain and return to Santosan.")
            return True
        else:
            slow_print("I'm sorry, that is incorrect.")
    
