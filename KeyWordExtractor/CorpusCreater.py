import os
from nltk.corpus.reader.plaintext import PlaintextCorpusReader

## Specifying the location of the Text Files of which the Corpus is to be made .
CorpusDir = 'DataSet/Text'
Corpus = PlaintextCorpusReader(CorpusDir, '.*')