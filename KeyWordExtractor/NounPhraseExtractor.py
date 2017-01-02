import nltk

## Defining some toy text
text = 'Commercial recommender systems use various data mining techniques to make appropriate recommendations to users during online, real-time sessions. Published algorithms focus more on the discrete user ratings instead of binary results, which hampers their predictive capabilities when usage data is sparse. The system proposed in this paper, e-VZpro, is an association mining-based recommender tool designed to overcome these problems through a two-phase approach. In the first phase, batches of customer historical data are analyzed through association mining in order to determine the association rules for the second phase. During the second phase, a scoring algorithm is used to rank the recommendations online for the customer. The second phase differs from the traditional approach and an empirical comparison between the methods used in e-VZpro and other collaborative filtering methods including dependency networks, item-based, and association mining is provided in this paper. This comparison evaluates the algorithms used in each of the above methods using two internal customer datasets and a benchmark dataset. The results of this comparison clearly show that e-VZpro performs well compared to dependency networks and association mining. In general, item-based algorithms with cosine similarity measures have the best performance.'

## Defining a Regex Expression for tokenizing the words .
sentence_re = r'''(?x)      # set flag to allow verbose regexps
      ([A-Z])(\.[A-Z])+\.?  # abbreviations, e.g. U.S.A.
    | \w+(-\w+)*            # words with optional internal hyphens
    | \$?\d+(\.\d+)?%?      # currency and percentages, e.g. $12.40, 82%
    | \.\.\.                # ellipsis
    | [][.,;"'?():-_`]      # these are separate tokens
'''