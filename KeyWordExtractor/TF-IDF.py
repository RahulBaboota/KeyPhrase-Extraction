"""


------------------------------   Creating the Different Models for TF-IDF   ------------------------------------------


"""

import nlkt
import sklearn
from sklearn.feature_extraction.text import CountVectorizer
from TextPreProcessing import TextTokenize
from TextPreProcessing import Extract_Candidates_Nouns
from TextPreProcessing import Extract_Candidates_Nouns_Adjective

## Defining Toy Text
Text = 'Rashid Siddiqui kept hearing those words from his fellow Muslim pilgrims lying mangled on the ground in 118-degree heat, under a searing Saudi sun. Barefoot, topless and dazed, Mr. Siddiqui had somehow escaped being crushed by the surging crowd.It was Sept. 24, 2015, the third morning of the hajj, the annual five-day pilgrimage to Mecca by millions of Muslims from around the world. By some estimates, it was the deadliest day in hajj history and one of the worst accidents in the world in decades.An American from Atlanta, Mr. Siddiqui, 42, had been walking through a sprawling valley of tens of thousands of pilgrim tents. His destination: Jamarat Bridge, where pilgrims throw pebbles at three large pillars in a ritual symbolizing the stoning of the devil. He was less than a mile from the bridge when the crush began.'

