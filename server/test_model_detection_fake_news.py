import json
import numpy as np
import re
import string
import nltk

nltk.download('stopwords')
nltk.download('punkt')

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
