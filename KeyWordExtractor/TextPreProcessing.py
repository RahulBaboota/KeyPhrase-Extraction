"""
--------------------------------------------    Data Preprocessing Steps   -----------------------------------------------------
"""

import nltk
from nltk import word_tokenize
from nltk import sent_tokenize
from nltk.corpus import stopwords




## Defining a Preprocessing class 

class DataPreprocess:

	def __init__(self,text):
		##


	## Defining a function to tokenize our text
	def TextTokenize(text):

		## Lowering the text
		text = text.lower()

		## Creating a list of Sentence Tokens
		sentence_tokens = sent_tokenize(text)

		## Creating a list of Word Tokens
		word_tokens = [word_tokenize(word) for word in sentence_tokens]

		## Removing stop words from the created word_tokens
		word_tokens = []

	## Defining a candidate extraction function which extracts all open words
	def ExtractCandidates1(word_tokens):





