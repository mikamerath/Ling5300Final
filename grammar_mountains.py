import re

from helpers import slow_print, get_player_response

# Noam Chomsky

def begin(finished=False):
    if finished:
        slow_print("You return to the Grammar Mountains satisfied upon seeing the labors of your work" +
                   "\nLooking around, you do not see anything interesting in the area and decide to return to Santosan")
        return True
    
    slow_print("You head towards the Grammar Mountains ")

def puzzle():
    slow_print("At the peak of the mountain, you find a tablet with the following inscriptions: " +
               "\nS -> NP VP" +
               "\nNP -> Det N | NP PP" +
               "\nVP -> V NP | V PP" +
               "\nPP -> P NP" + 
               "\nDet -> a | the" +
               "\nN -> thing | person | hill | man | woman" + 
               "\nV -> walked | saw | ate" +
               "\nP -> up | on | in")