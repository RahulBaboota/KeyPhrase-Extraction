"""

------------------------------   Creating the Noun Phrase Extractor   ------------------------------------------

"""

import nltk
import itertools
import string
from TextPreProcessing import TextTokenize
from TextPreProcessing import Extract_Candidates_Nouns_Adjective

## For Key Phrase Extraction , we first need to extract possible candidates which could be labelled as Keywords / KeyPhrases .
## Assigning all of the words as KeyWords would be an extremely bruteForce method which would ultimately end up in poor
## results . As a result , we will extract Noun Phrases from our text which will be the candidates for KeyWords .

## Defining toy Text .
Text = "Commercial recommender systems use various data mining techniques to make appropriate recommendations to users during online, real-time sessions. Published algorithms focus more on the discrete user ratings instead of binary results, which hampers their predictive capabilities when usage data is sparse. The system proposed in this paper, e-VZpro, is an association mining-based recommender tool designed to overcome these problems through a two-phase approach. In the first phase, batches of customer historical data are analyzed through association mining in order to determine the association rules for the second phase. During the second phase, a scoring algorithm is used to rank the recommendations online for the customer. The second phase differs from the traditional approach and an empirical comparison between the methods used in e-VZpro and other collaborative filtering methods including dependency networks, item-based, and association mining is provided in this paper. This comparison evaluates the algorithms used in each of the above methods using two internal customer datasets and a benchmark dataset. The results of this comparison clearly show that e-VZpro performs well compared to dependency networks and association mining. In general, item-based algorithms with cosine similarity measures have the best performance."

"""
------------------------------   Defining Some Global Variables   ------------------------------------------
"""

## Remove all those tokens which are stop words or entirely punctuation .
Punctuation = set(string.punctuation)
Stop_Words = set(nltk.corpus.stopwords.words('english'))

## This matches any number of adjectives followed by at least one noun that may be joined by a preposition to one other adjective(s)+noun(s) sequence .
Grammar = r'KT: {(<JJ>* <NN.*>+ <IN>)? <JJ>* <NN.*>+}'

"""
------------------------------   Creating Noun-Phrase Chunker Extractor   ------------------------------------------
"""

## We will now make a function that extracts the candidate chunks from our text .
def Extract_Candidate_Chunks(Text , Grammar):

    ## Defining a Chunker based on the Grammar we defined above .
    Chunker = nltk.chunk.regexp.RegexpParser(Grammar)
    ## Assigning POS Tags .
    Tagged_Sentences = nltk.pos_tag_sents( nltk.word_tokenize(sentence) for sentence in nltk.sent_tokenize(Text) )

    ## Gathering the Chunks made by the Chunker from the Tree created .
    Chunks = list(itertools.chain.from_iterable(nltk.chunk.tree2conlltags(Chunker.parse(Tagged_Sentences)) for Tagged_Sentences in Tagged_Sentences))

    ## We will now join the chunk words into a single Chunked Phrase .
    Candidates = [' '.join(Word for Word, Pos, Chunk in Group).lower() for Key, Group in itertools.groupby(Chunks, lambda (Word,Pos,Chunk): Chunk != 'O') if Key]

    return [ Candidate for Candidate in Candidates if Candidate not in Stop_Words and not all(Char in Punctuation for Char in Candidate)]

"""
------------------------------   Extracting Nouns and Adjectives   ------------------------------------------
"""

def Extract_Candidate_Words(Text) :

    ## Tokenizing the text
    Text_Tokens = TextTokenize(Text)

    ## Extracting the candidates from the created tokens which in this case is "nouns" and "adjectives" .
    Candidates_Nouns_Adjectives = Extract_Candidates_Nouns_Adjective(Text_Tokens)

    return Candidates_Nouns_Adjectives