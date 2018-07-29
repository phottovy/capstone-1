import string
from nltk.corpus import stopwords

def nltk_s_words():
    '''
    Remove punctuation from nltk's stopwords list
    '''
    s_words = stopwords.words('english')
    return [''.join([char for char in word if char not in string.punctuation]) for word in s_words]

def add_stop_words():
    '''
    A list of additional stop words.
    '''
    additional_s_words = ["aren't",
                          "can't",
                          "couldn't",
                          'did',
                          "didn't",
                          'does',
                          "doesn't",
                          'doing',
                          "don't",
                          "hadn't",
                          "hasn't",
                          "haven't",
                          'having',
                          "he'd",
                          "he'll",
                          "he's",
                          "here's",
                          "how's",
                          "i'd",
                          "i'll",
                          "i'm",
                          "i've",
                          "isn't",
                          "it's",
                          "let's",
                          "mustn't",
                          'ought',
                          'ours',
                          'ourselves',
                          "shan't",
                          "she'd",
                          "she'll",
                          "she's",
                          "shouldn't",
                          "that's",
                          'theirs',
                          "there's",
                          "they'd",
                          "they'll",
                          "they're",
                          "they've",
                          "wasn't",
                          "we'd",
                          "we'll",
                          "we're",
                          "we've",
                          "weren't",
                          "what's",
                          "when's",
                          "where's",
                          "who's",
                          "why's",
                          "won't",
                          "wouldn't",
                          "you'd",
                          "you'll",
                          "you're",
                          "you've"]
    return [''.join([char for char in word if char not in string.punctuation]) for word in additional_s_words]
