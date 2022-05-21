import json
import numpy as np
import re
import string
import nltk

nltk.download('stopwords')
nltk.download('punkt')

from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()

# probability threshold
ERROR_THRESHOLD = 0.2
# load our calculated synapse values
synapse_file = 'M25000epouchs.json'
with open(synapse_file) as data_file:
    synapse = json.load(data_file)
    synapse_0 = np.asarray(synapse['synapse0'])
    synapse_1 = np.asarray(synapse['synapse1'])

with open('M25000epouchs.txt', 'r') as f:
    words = f.read().splitlines()

classes = ['real', 'fake']

def remove_mentions(tweet):
  return re.sub(r'@\w+', '', tweet)

def remove_urls(tweet):
  return re.sub(r'http.?://[^\s]+[\s]?', '', tweet)

def inders_oneword(tweet):
  # By compressing the underscore, the emoji is kept as one word
  return tweet.replace('_','')

def remove_emoji(tweet):
  emoji_pattern = re.compile("["
                           u"\U0001F600-\U0001F64F"  # emoticons
                           u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                           u"\U0001F680-\U0001F6FF"  # transport & map symbols
                           u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           u"\U00002702-\U000027B0"
                           u"\U000024C2-\U0001F251"
                           "]+", flags=re.UNICODE)
  return emoji_pattern.sub(r'', tweet)

def remove_punctuation(tweet):
  # Make translation table
  punct = string.punctuation
  # Every punctuation symbol will be replaced by a space
  trantab = str.maketrans(punct, len(punct)*' ')
  return tweet.translate(trantab)

def remove_digits(tweet):
  return re.sub('\d+', '', tweet)

def to_lower(tweet):
  return tweet.lower()

def remove_stopwords(tweet):
  stopwords_list = stopwords.words('english')
  # Some words which might indicate a certain sentiment are kept via a whitelist
  whitelist = ["n't", "not", "no"]
  words = tweet.split()
  clean_words = [word for word in words if (word not in stopwords_list or word in whitelist) and len(word) > 1]
  return " ".join(clean_words)

def stemming(tweet):
  porter = PorterStemmer()
  words = tweet.split()
  stemmed_words = [porter.stem(word) for word in words]
  return " ".join(stemmed_words)

def cleaning(tweet):
  tweet = remove_mentions(tweet)
  tweet = remove_urls(tweet)
  tweet = remove_emoji(tweet)
  tweet = inders_oneword(tweet)
  tweet = remove_punctuation(tweet)
  tweet = remove_digits(tweet)
  tweet = to_lower(tweet)
  tweet = remove_stopwords(tweet)
  tweet = stemming(tweet)
  return tweet;

  # compute sigmoid nonlinearity
def sigmoid(x):
    output = 1/(1+np.exp(-x))
    return output

def clean_up_sentence(sentence):
    sentence = cleaning(sentence)
    # tokenize the pattern
    sentence_words = nltk.word_tokenize(sentence)
    # stem each word
    sentence_words = [stemmer.stem(word.lower()) for word in sentence_words]
    return sentence_words

# return bag of words array: 0 or 1 for each word in the bag that exists in the sentence
def bow(sentence, words, show_details=False):
    # tokenize the pattern
    sentence_words = clean_up_sentence(sentence)
    # bag of words
    bag = [0]*len(words)
    for s in sentence_words:
        for i,w in enumerate(words):
            if w == s:
                bag[i] = 1
                if show_details:
                    print ("found in bag: %s" % w)

    return(np.array(bag))