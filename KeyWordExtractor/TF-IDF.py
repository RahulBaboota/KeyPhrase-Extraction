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
Text = ['Rashid Siddiqui kept hearing those words from his fellow Muslim pilgrims lying mangled on the ground in 118-degree heat, under a searing Saudi sun. Barefoot, topless and dazed, Mr. Siddiqui had somehow escaped being crushed by the surging crowd.It was Sept. 24, 2015, the third morning of the hajj, the annual five-day pilgrimage to Mecca by millions of Muslims from around the world. By some estimates, it was the deadliest day in hajj history and one of the worst accidents in the world in decades.An American from Atlanta, Mr. Siddiqui, 42, had been walking through a sprawling valley of tens of thousands of pilgrim tents. His destination: Jamarat Bridge, where pilgrims throw pebbles at three large pillars in a ritual symbolizing the stoning of the devil. He was less than a mile from the bridge when the crush began.']

## Breaking the test into individual sentences to act as input to CountVectorizer Class .

# Declaring a list to hold the sentence tokens created from the tokens .
Sentence_Tokens = sent_tokenize(Text[0])

"""
-----------------------------------------  Creating Model with open words ----------------------------------------------------
"""

def TF_IDF_Baseline(Text):

    ## Creating a dictionary of vocabulary to create a Vector Space Model to represent words as "Vectors."

    Count_Vectorizer = CountVectorizer(stop_words="english")
    Count_Vectorizer.fit_transform(Text)
    Vocabulary = Count_Vectorizer.vocabulary_
    Vocabulary = OrderedDict(sorted(Vocabulary.items(), reverse=False, key=lambda t: t[1]))

    # print Vocabulary

    # Creating the vector in our Vector Space Model with the help of the above created dictionary .
    # It is important to note that herein we are creating a single vector which makes records of frequency count for the tokens
    # in the entire article .
    TF_Matrix = Count_Vectorizer.transform(Text).todense()
    TF_Matrix = normalize(TF_Matrix, norm="l1", axis=1)

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

    








TF_IDF_Baseline(Text)