import nltk
import re

from helpers import get_player_response, slow_print
import helpers


# Claude Shannon: first reference to n grams

BIGRAM_PASS_PHRASE_NUM = 0

def begin(finished=False):
    if finished:
        slow_print("The familiar words of Claushe Dannon echo through your mind \"Remember that the words you say are connected, their meaning will carry you through the rest of your journey\"")
        return True
    
    if helpers.get_player_word_count() < 25:
       slow_print("You are not ready to reflect on your journey yet. Please return here when you have explored the other areas in greater detail.")
       slow_print("Defeated, you head back towards Santosan.")
       return False

    slow_print("As you arrive at the Forest of connection, you find a man sitting underneath a tree, drinking from a jug."
               + "\nHe gestures for you to sit down next to him. As he notices you approaching he remarks, \"It seems you are ready to reflect on your journey\"")
    
    return puzzle()
    
    

def puzzle():
    solved_counts = False
    while True:
        attempts = 0
        response = helpers.tokenize(get_player_response("\"To start, what are any of the 5 most common words you've used on your journey?\""))
        for word in response:
            if word.lower() in [x[0] for x in helpers.get_n_most_common_words(5)]:
                solved_counts = True
                break

        attempts += 1
        if not solved_counts and attempts < 3:
            slow_print("Please try again, think of the common words you've been using.")
        else:
            break
    
    if not solved_counts:
        slow_print("It seems that you do not know yourself well enough to complete this challenge." +
                   "\nCome back after you understand how you interact with others around you." +
                   "\n\nDefeated, you head back to Santosan.")
        return False
    
    slow_print("You seem to have a solid understanding of the words you have used to communicate!")
    
    while True:
        num_words = helpers.get_player_word_count()
        response = helpers.tokenize(get_player_response("You have currently communicated " + str(num_words) + " words. How many bigrams could that be?"))
        if str(num_words - 1) in response:
            break
        elif re.match(r"[\w\s]*([Gg]ive up|[Ll]eave|[Ss]mash|[Qq]uit|[Ee]xit)[\w\s]*", response):
            slow_print("Frustrated, you give up with the puzzle and start heading back to Santosan")
            return False
        else:
            slow_print("That is incorrect, remember the relationship between the number of bigrams and the number of words")

    slow_print("Congratulations on understanding the relationship between total words and total possible bigrams." +
               "\nSatisfied with your answers, the man tells you his secret:" +
               "\n" + "\"" + helpers.pass_phrases[BIGRAM_PASS_PHRASE_NUM] + "\"" +
               "\nWith a skip in your step, you return to Santosan")
    helpers.add_pass_phrase_to_player(BIGRAM_PASS_PHRASE_NUM)

    return True