"""
--------------------------------------------    Data Preprocessing Steps   -----------------------------------------------------
"""

import nltk
from nltk import word_tokenize
from nltk import sent_tokenize
from nltk.corpus import stopwords
from string import punctuation




## Defining a Preprocessing class 

class DataPreprocess:

    def __init__(self):
        
        self._StopWords = set(stopwords.words("english") + list(punctuation))

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
                if word_tokens[i][j] not in self._StopWords:
                    word_tokens_filtered.append(word_tokens[i][j])
                else:
                    continue

        return word_tokens_filtered
        


    ## Defining a candidate extraction function which extracts all open words
    def ExtractCandidates1(word_tokens):

        





