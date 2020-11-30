import unicodedata
import re
import json

import nltk
from nltk.tokenize.toktok import ToktokTokenizer
from nltk.corpus import stopwords

import pandas as pd

from acquire import get_all_blogs, get_all_news

def basic_clean(s):
    s = s.lower()
    s = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode('utf-8', 'ignore')
    s = re.sub(r"[^a-z0-9'\s]", '', s)
    return s

def tokenize(s):
    tokenizer = ToktokTokenizer()
    return tokenizer.tokenize(s, return_str=True)

def stem(s):
    ps = nltk.porter.PorterStemmer()
    stems = [ps.stem(word) for word in s.split()]
    article_stemmed = ' '.join(stems)
    return article_stemmed

def lemmatize(s):
    wnl = nltk.stem.WordNetLemmatizer()
    lemmas = [wnl.lemmatize(word) for word in s.split()]
    article_lemmatized = ' '.join(lemmas)
    return article_lemmatized

def remove_stopwords(s):
    stopword_list = stopwords.words('english')
    stopword_list.remove('no')
    stopword_list.remove('not')
    words = s.split()
    filtered_words = [w for w in words if w not in stopword_list]
    article_substopwords = ' '.join(filtered_words)
    return article_substopwords