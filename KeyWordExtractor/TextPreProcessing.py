"""


--------------------------------------------    Data Preprocessing Steps   -----------------------------------------------------


"""

import nltk
from nltk import word_tokenize
from nltk import sent_tokenize
from nltk import pos_tag
from nltk.corpus import stopwords
from string import punctuation
import re

"""
--------------------------------------------    Tokenizing The Text   -----------------------------------------------------
"""

## Defining a set of Stopwords to remove from our input text
StopWords = set(stopwords.words("english") + list(punctuation))

## Defining a function to tokenize our text
def TextTokenize(Text):

    ## Lowering the text
    Text = Text.lower()

    ## Creating a list of Sentence Tokens
    sentence_tokens = sent_tokenize(Text)

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


"""
-----------------------------------------  Defining Candidate Extraction Rules ----------------------------------------------------
"""

## For creating a baseline model , we dont' define any kind of grammar rules for extracting the candidate keywords and simply make ## all the tokens as the candidates . Therefore , there isn't any kind of function required to do this task .

## Next , we will define a function which extracts candidates for keywords wherein the candidate selection criterion is set to 
## "nouns only."

def Extract_Candidates_Nouns(Text_tokens):

    ## Assigning the appropriate pos_tag to each token
    pos_tagged_tokens = pos_tag(Text_tokens)

    ## Creating a list which will hold the candidates
    Noun_Candidates = []

    ##Defining the Regular Expression for extracting nouns
    noun_pattern = r"^NN?."

    ## Looping over the pos_tagged tuple to extract nouns
    for token_tag_pair in pos_tagged_tokens:
        if(re.match(noun_pattern,token_tag_pair[1])):
            Noun_Candidates.append(token_tag_pair[0])

    return Noun_Candidates

## Next , we will define a function which extracts candidates for keywords wherein the candidate selection criterion is set to 
## "nouns and adjectves".

def Extract_Candidates_Nouns_Adjective(Text_tokens):

    ## Assigning the appropriate pos_tag to each token
    pos_tagged_tokens = pos_tag(Text_tokens)

    ## Creating a list which will hold the candidates
    Noun_Adjective_Candidates = []

    ##Defining the Regular Expression for extracting adjectives
    adjective_pattern = r"^JJ?."

    ##Defining the Regular Expression for extracting nouns
    noun_pattern = r"^NN?."

    ## Looping over the pos_tagged tuple to extract nouns and adjectives
    for token_tag_pair in pos_tagged_tokens:
        if( re.match(noun_adjective_pattern,token_tag_pair[1]) or re.match(noun_pattern,token_tag_pair[1])):
            Noun_Adjective_Candidates.append(token_tag_pair[0])

    return Noun_Adjective_Candidates

#-----------------------------------------------------------------------------------------------------------------------------------