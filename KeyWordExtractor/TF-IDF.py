"""


------------------------------   Creating the Different Models for TF-IDF   ------------------------------------------


"""

import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from nltk import sent_tokenize
from TextPreProcessing import TextTokenize
from TextPreProcessing import Extract_Candidates_Nouns
from TextPreProcessing import Extract_Candidates_Nouns_Adjective

## Defining Toy Text
Text = 'Rashid Siddiqui kept hearing those words from his fellow Muslim pilgrims lying mangled on the ground in 118-degree heat, under a searing Saudi sun. Barefoot, topless and dazed, Mr. Siddiqui had somehow escaped being crushed by the surging crowd.It was Sept. 24, 2015, the third morning of the hajj, the annual five-day pilgrimage to Mecca by millions of Muslims from around the world. By some estimates, it was the deadliest day in hajj history and one of the worst accidents in the world in decades.An American from Atlanta, Mr. Siddiqui, 42, had been walking through a sprawling valley of tens of thousands of pilgrim tents. His destination: Jamarat Bridge, where pilgrims throw pebbles at three large pillars in a ritual symbolizing the stoning of the devil. He was less than a mile from the bridge when the crush began.'

## Breaking the test into individual sentences to act as input to CountVectorizer Class .

# Declaring a list to hold the sentence tokens created from the tokens .
Sentence_Tokens = sent_tokenize(Text)

"""
-----------------------------------------  Creating Model with open words ----------------------------------------------------
"""

def TF_IDF_Candidates_All(Text):

    ## Creating a dictionary of vocabulary to create a Vector Space Model to represent words as "Vectors."

    Count_Vectorizer = CountVectorizer(stop_words="english")
    Count_Vectorizer.fit_transform(Sentence_Tokens)
    # print "Vocabulary:", Count_Vectorizer.vocabulary_

    ## Creating the vectors in our Vector Space Model with the help of the above created dictionary
    Word_Vectors = Count_Vectorizer.transform(Sentence_Tokens).todense()
    # print Word_Vectors

    ## Instantiating the TF-IDF Transformer to assign weights to each word.

    TFIDF = TfidfTransformer(norm="l2")
    TFIDF.fit(Word_Vectors)
    TFIDF_matrix = TFIDF.transform(Word_Vectors)
    # print TFIDF_matrix.todense()


TF_IDF_Candidates_All(Text)