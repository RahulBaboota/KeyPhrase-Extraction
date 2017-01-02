"""


------------------------------   Creating the Different Models for TF-IDF   ------------------------------------------


"""

import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.preprocessing import normalize
from nltk import sent_tokenize
from collections import OrderedDict
from TextPreProcessing import TextTokenize
from TextPreProcessing import Extract_Candidates_Nouns
from TextPreProcessing import Extract_Candidates_Nouns_Adjective
import numpy as np

## Defining Toy Text
Text = ['Rashid Siddiqui kept hearing those words from his fellow Muslim pilgrims lying mangled on the ground in 118 degree heat, under a searing Saudi sun. Barefoot, topless and dazed, Mr. Siddiqui had somehow escaped being crushed by the surging crowd. It was Sept. 24, 2015, the third morning of the hajj, the annual five day pilgrimage to Mecca by millions of Muslims from around the world. By some estimates, it was the deadliest day in hajj history and one of the worst accidents in the world in decades. An American from Atlanta, Mr. Siddiqui, 42, had been walking through a sprawling valley of tens of thousands of pilgrim tents. His destination: Jamarat Bridge, where pilgrims throw pebbles at three large pillars in a ritual symbolizing the stoning of the devil. He was less than a mile from the bridge when the crush began.']

## Breaking the test into individual sentences to act as input to CountVectorizer Class .

# Declaring a list to hold the sentence tokens created from the tokens .
Sentence_Tokens = sent_tokenize(Text[0])

"""
-----------------------------------------  Creating TF-IDF Model with variations -------------------------------------------------
"""

def TF_IDF(Text,norm="l2",term_frequency="default"):

    ## Creating a dictionary of vocabulary to create a Vector Space Model to represent words as "Vectors."

    Count_Vectorizer = CountVectorizer(stop_words="english")
    Count_Vectorizer.fit_transform(Text)
    Vocabulary = Count_Vectorizer.vocabulary_
    Vocabulary = OrderedDict(sorted(Vocabulary.items(), reverse=False, key=lambda t: t[1]))

    # print Vocabulary

    # Creating the vector in our Vector Space Model with the help of the above created dictionary .
    # It is important to note that herein we are creating a single vector which makes records of frequency count for the tokens
    # in the entire article .

    ## In this case , we consider the default term frequency term which is simply the number of times a token appears in the text.
    if (term_frequency=="default"):
        TF_Matrix = Count_Vectorizer.transform(Text).todense()
        TF_Matrix = normalize(TF_Matrix, norm=norm, axis=1)

        # print TF_Matrix

    ## In this case , we consider the logarithmic term frequency which helps to smoothes the noise and squishes the range down.
    elif (term_frequency=="logarithmic"):
        TF_Matrix = Count_Vectorizer.transform(Text).todense()
        TF_Matrix = TF_Matrix + 1
        TF_Matrix = np.log(TF_Matrix)
        TF_Matrix = normalize(TF_Matrix, norm=norm, axis=1)

        # print TF_Matrix

    # Creating the vector for each document (sentence) for helping us evaluate the idf weight for each matrix .
    IDF_Help = Count_Vectorizer.transform(Sentence_Tokens).todense()

    # print IDF_Help

    ## Instantiating the TF-IDF Transformer to compute idf weights for each word.
    TFIDF = TfidfTransformer()
    TFIDF.fit(IDF_Help)
    IDF_Matrix = TFIDF.idf_

    # print IDF_Matrix

    ## Converting the IDF_Matrix to a square diagonal matrix for vector multiplication with TF_Matrix Matrix to evaluate
    ## the resulting matrix with final scores .
    IDF_Square_Matrix = np.diag(IDF_Matrix)

    # print IDF_Square_Matrix

    ## Multiplying Matrices "TF_Matrix" and "IDF_Square_Matrix" to obtain the final matrix with final weighted scores .
    Final_Weight_Matrix = np.dot(TF_Matrix,IDF_Square_Matrix)

    # print Final_Weight_Matrix.shape
    # print Final_Weight_Matrix

    ## Storing the weights of the final score matrix in a list
    Final_Weight_Matrix_Scores = []

    for i in range(0,Final_Weight_Matrix.shape[1]):
        Final_Weight_Matrix_Scores.append(Final_Weight_Matrix[0,i])

    # print Final_Weight_Matrix_Scores

    ## Storing the vocabulary words in a list for iterating over this and Final_Weight_Matrix_Scores list simultaneously
    Vocabulary_Words = []

    for key in Vocabulary:
        Vocabulary_Words.append(key)

    # print Vocabulary_Words

    ## Creating a resultant dictionary to be returned containing the token as the key and it's score as it's value .
    TF_IDF_Scores = {}

    for token,score in zip(Vocabulary_Words,Final_Weight_Matrix_Scores):
        TF_IDF_Scores[token] = score

    ## Converting the dictionary into an ordered dictionary in descending order .
    TF_IDF_Scores = OrderedDict(sorted(TF_IDF_Scores.items(), reverse=True, key=lambda t: t[1]))

    return TF_IDF_Scores


"""
-----------------------------------------  Creating Model with open words ----------------------------------------------------
"""

## Herein , we are creating a model with open words that is we are not trimming / pruning any of the original text except for
## the stop words . Therefore , in practice , the model with open words will simply be the above created function for evaluating
## TF-IDF Scores .

def TF_IDF_Candidates_All(Text,norm,term_frequency):

    ## Simply returning the original function created above to do the same .
    TF_IDF(Text,norm=norm,term_frequency=term_frequency)


"""
-----------------------------------------  Creating Model with Nouns ----------------------------------------------------
"""

def TF_IDF_Candidates_Nouns(Text,norm,term_frequency):

    All_Tokens_Scores = TF_IDF(Text,norm=norm,term_frequency=term_frequency)

    ## Storing the Text Tokens in a list
    Text_Tokens = []

    for key in All_Tokens_Scores:
        Text_Tokens.append(key)

    ## Extracting the candidates from the created tokens which in this case is "nouns" .
    Candidates_Nouns = Extract_Candidates_Nouns(Text_Tokens)

    ## Defining a list to hold the keys to be deleted from the original dictionary .
    Delete_Keys = []

    for token in Text_Tokens:
        if  token in Candidates_Nouns:
            continue
        else:
            Delete_Keys.append(token)

    ## Deleting the undesired keys from the original dictionary .
    for token in Delete_Keys:
        del All_Tokens_Scores[token]

    ## Making a copy of the modified original dictionary to a new dictionary to be returned
    Scores_Candidates_Nouns = All_Tokens_Scores

    return Scores_Candidates_Nouns

"""
-----------------------------------------  Creating Model with Nouns ----------------------------------------------------
"""

def TF_IDF_Candidates_Nouns_Adjectives(Text,norm,term_frequency):

    All_Tokens_Scores = TF_IDF(Text,norm=norm,term_frequency=term_frequency)

    ## Storing the Text Tokens in a list
    Text_Tokens = []

    for key in All_Tokens_Scores:
        Text_Tokens.append(key)

    ## Extracting the candidates from the created tokens which in this case is "nouns" .
    Candidates_Nouns_Adjective = Extract_Candidates_Nouns_Adjective(Text_Tokens)

    ## Defining a list to hold the keys to be deleted from the original dictionary .
    Delete_Keys = []

    for token in Text_Tokens:
        if  token in Candidates_Nouns_Adjective:
            continue
        else:
            Delete_Keys.append(token)

    ## Deleting the undesired keys from the original dictionary .
    for token in Delete_Keys:
        del All_Tokens_Scores[token]

    ## Making a copy of the modified original dictionary to a new dictionary to be returned
    Scores_Candidates_Nouns_Adjectives = All_Tokens_Scores

    return Scores_Candidates_Nouns_Adjectives

#-----------------------------------------------------------------------------------------------------------------------------------