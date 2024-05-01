import re

import helpers

unary_rules = ["Det -> a", "Det -> the",
               "N -> thing", "N -> person", "N -> hill", "N -> man", "N -> woman", 
               "V -> walked", "V -> saw", "V -> ate",
               "P -> up", "P -> on", "P -> in"]

binary_rules = ["S -> NP VP",
               "NP -> Det N",
               "NP -> NP PP",
               "VP -> V NP",
               "VP -> V PP",
               "PP -> P NP"]


def cky_parse(sentence):
    tokenized_sentence = helpers.tokenize(sentence.lower())
    result = [["None"]*(len(tokenized_sentence)+1) for i in range(len(tokenized_sentence))]
    for i in range(len(tokenized_sentence)):
        result[i][i+1] = tokenized_sentence[i]
    
    for pos in range(1,len(tokenized_sentence)+1):
        for i in range(0, len(tokenized_sentence) - pos + 1):
            j = i + pos
            for rule in unary_rules:
                B = re.match(r"\w+ -> (\w+)", rule).group(1)
                if result[i][j] == B:
                    result[i][j] = re.match(r"^(.*?) ->", rule).group(1)

            
            for k in range(i+1, j):
                for rule in binary_rules:
                    B = re.match(r"\w+ -> (\w+) (\w+)", rule).group(1)
                    C = re.match(r"\w+ -> (\w+) (\w+)", rule).group(2)
                    if result[i][k] == B and result[k][j] == C:
                        result[i][j] = re.match(r"^(.*?) ->", rule).group(1)

    return result

def is_sentence(sentence):
    result_array = cky_parse(sentence)
    # Only return true if the entire input string is a sentence
    if result_array[0][len(result_array)] == "S":
        return True
    return False