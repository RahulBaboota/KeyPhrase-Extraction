import nltk
from nltk import pos_tag
from TextPreProcessing import TextTokenize

## Defining some toy text
Text = 'Commercial recommender systems use various data mining techniques to make appropriate recommendations to users during online, real-time sessions. Published algorithms focus more on the discrete user ratings instead of binary results, which hampers their predictive capabilities when usage data is sparse. The system proposed in this paper, e-VZpro, is an association mining-based recommender tool designed to overcome these problems through a two-phase approach. In the first phase, batches of customer historical data are analyzed through association mining in order to determine the association rules for the second phase. During the second phase, a scoring algorithm is used to rank the recommendations online for the customer. The second phase differs from the traditional approach and an empirical comparison between the methods used in e-VZpro and other collaborative filtering methods including dependency networks, item-based, and association mining is provided in this paper. This comparison evaluates the algorithms used in each of the above methods using two internal customer datasets and a benchmark dataset. The results of this comparison clearly show that e-VZpro performs well compared to dependency networks and association mining. In general, item-based algorithms with cosine similarity measures have the best performance.'

## Optional Stemmer and Lemmatizer .
Lemmatizer = nltk.WordNetLemmatizer()
Stemmer = nltk.stem.porter.PorterStemmer()

## Defining Grammar for extracting Noun Phrases .
Grammar = r"""
    NBAR:
        {<NN.*|JJ>*<NN.*>}  # Nouns and Adjectives, terminated with Nouns

    NP:
        {<NBAR>}
        {<NBAR><IN><NBAR>}  # Above, connected with in/of/etc...
"""

## Breaking the input text into individual tokens .
Tokens = TextTokenize(Text)

## Assigning the POS Tags .
pos_tagged_tokens = pos_tag(Tokens)

## Defining a Chunker based on the Grammar for extracting Noun Phrases .
Chunker = nltk.RegexpParser(Grammar)