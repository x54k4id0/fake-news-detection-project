import json
import numpy as np

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
