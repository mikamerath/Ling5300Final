import helpers

import cky

helpers.add_player_string_to_counts("This is the player counts, does it work? I'm adding the word again and this is the word")

print(helpers.get_n_most_common_words(3))
print("The word frequency of the: " + str(helpers.get_word_frequency("the")))
print("The most common bigrams are: " + str(helpers.get_n_most_common_bigrams(3)))
print("Getting bigram frequency of the word: " + str(helpers.get_bigram_frequency("the", "word")))

helpers.add_pass_phrase_to_player(1)


# Sentences in the grammar
print("The following sentences should return true:")
print(cky.is_sentence("a person walked up the hill"))
print(cky.is_sentence("the person walked on the person"))
print(cky.is_sentence("a hill up a thing up the woman saw in a woman"))

# Not sentences in the grammar
print("The following sentences should return false:")
print(cky.is_sentence("the person saw the man on the hill on the thing walked a hill up a thing up the woman saw in a woman"))
print(cky.is_sentence("the person saw the man on the hill on the thing walked a hill up a thing up the woman a saw in a woman"))