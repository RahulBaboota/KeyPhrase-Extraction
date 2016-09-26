"""


------------------------------   Creating the Different Models for Baseline   ------------------------------------------


"""

import nltk
from collections import defaultdict
from collections import OrderedDict
from TextPreProcessing import TextTokenize
from TextPreProcessing import Extract_Candidates_Nouns
from TextPreProcessing import Extract_Candidates_Nouns_Adjective

## Defining Toy Text
Text = 'Rashid Siddiqui kept hearing those words from his fellow Muslim pilgrims lying mangled on the ground in 118-degree heat, under a searing Saudi sun. Barefoot, topless and dazed, Mr. Siddiqui had somehow escaped being crushed by the surging crowd.It was Sept. 24, 2015, the third morning of the hajj, the annual five-day pilgrimage to Mecca by millions of Muslims from around the world. By some estimates, it was the deadliest day in hajj history and one of the worst accidents in the world in decades.An American from Atlanta, Mr. Siddiqui, 42, had been walking through a sprawling valley of tens of thousands of pilgrim tents. His destination: Jamarat Bridge, where pilgrims throw pebbles at three large pillars in a ritual symbolizing the stoning of the devil. He was less than a mile from the bridge when the crush began.'

"""
-----------------------------------------  Creating Model with open words ----------------------------------------------------
"""

def Baseline_Candidates_All(Text):

    ## When we are creating our model with open words (all words) , the candidates in this case are all the tokens . 
    Candidates_All = TextTokenize(Text)

    ## Initialising a dictionary to map the tokens with their frequencies .
    Frequency_Candidates_All = defaultdict(int)

    ## Looping over the tokens to map them with their frequencies .
    for token in Candidates_All:
        Frequency_Candidates_All[token] += 1

    ## Sorting the tokens in descending order based on their frequencies .
    Frequency_Candidates_All = OrderedDict(sorted(Frequency_Candidates_All.items(), reverse=True, key=lambda t: t[1]))

    return Frequency_Candidates_All

"""
-----------------------------------------  Creating Model with Nouns ----------------------------------------------------
"""

def Baseline_Nouns(Text):

    ## Tokenizing the text
    Text_Tokens = TextTokenize(Text)

    ## Extracting the candidates from the created tokens which in this case is "nouns"
    Candidates_Nouns = Extract_Candidates_Nouns(Text_Tokens)

    ## Initialising a dictionary to map the tokens with their frequencies .
    Frequency_Candidates_Nouns = defaultdict(int)

    ## Looping over the tokens to map them with their frequencies .
    for token in Candidates_Nouns:
        Frequency_Candidates_Nouns[token] += 1

    ## Sorting the tokens in descending order based on their frequencies .
    Frequency_Candidates_Nouns = OrderedDict(sorted(Frequency_Candidates_Nouns.items(), reverse=True, key=lambda t: t[1]))

    return Frequency_Candidates_Nouns

"""
---------------------------------------  Creating Model with Nouns and Adjectives --------------------------------------------------
"""

def Baseline_Nouns_Adjectives(Text):

    ## Tokenizing the text
    Text_Tokens = TextTokenize(Text)

    ## Extracting the candidates from the created tokens which in this case is "nouns"
    Candidates_Nouns_Adjectives = Extract_Candidates_Nouns_Adjective(Text_Tokens)

    ## Initialising a dictionary to map the tokens with their frequencies .
    Frequency_Candidates_Nouns_Adjectives = defaultdict(int)

    ## Looping over the tokens to map them with their frequencies .
    for token in Candidates_Nouns_Adjectives:
        Frequency_Candidates_Nouns_Adjectives[token] += 1

    ## Sorting the tokens in descending order based on their frequencies .
    Frequency_Candidates_Nouns_Adjectives = OrderedDict(sorted(Frequency_Candidates_Nouns_Adjectives.items(), reverse=True, key=lambda t: t[1]))

    return Frequency_Candidates_Nouns_Adjectives

#-----------------------------------------------------------------------------------------------------------------------------------