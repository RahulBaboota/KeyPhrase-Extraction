"""
--------------------------------------------    Data Preprocessing Steps   -----------------------------------------------------
"""

import nltk
from nltk import word_tokenize
from nltk import sent_tokenize
from nltk.corpus import stopwords
from string import punctuation
from collections import defaultdict


StopWords = set(stopwords.words("english") + list(punctuation))

## Defining a function to tokenize our text
def TextTokenize(text):

    ## Lowering the text
    text = text.lower()

    ## Creating a list of Sentence Tokens
    sentence_tokens = sent_tokenize(text)

    ## Creating a list of Word Tokens
    word_tokens = [word_tokenize(word) for word in sentence_tokens]

    ## Removing stop words from the created word_tokens
    word_tokens_filtered = []
    no_of_sentences = len(word_tokens)  

    for i in range(0,no_of_sentences):
        no_of_tokens = len(word_tokens[i])
        for j in range(0,no_of_tokens):
            if word_tokens[i][j] not in StopWords:
                word_tokens_filtered.append(word_tokens[i][j])
            else:
                continue

    return word_tokens_filtered

text = 'Rashid Siddiqui kept hearing those words from his fellow Muslim pilgrims lying mangled on the ground in 118-degree heat, under a searing Saudi sun. Barefoot, topless and dazed, Mr. Siddiqui had somehow escaped being crushed by the surging crowd.It was Sept. 24, 2015, the third morning of the hajj, the annual five-day pilgrimage to Mecca by millions of Muslims from around the world. By some estimates, it was the deadliest day in hajj history and one of the worst accidents in the world in decades.An American from Atlanta, Mr. Siddiqui, 42, had been walking through a sprawling valley of tens of thousands of pilgrim tents. His destination: Jamarat Bridge, where pilgrims throw pebbles at three large pillars in a ritual symbolizing the stoning of the devil.He was less than a mile from the bridge when the crush began.'

TextTokenize(text)







