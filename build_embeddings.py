#!/usr/bin/env python

import fasttext, os
from gensim.models.word2vec import LineSentence, Word2Vec

MODELS_DIR = os.path.join(os.path.dirname(__file__), 'models')
DATA_FILE = os.path.join(os.path.dirname(__file__), 'data', 'all_texts_clean.txt')

if not os.path.exists(MODELS_DIR):
    os.makedirs(MODELS_DIR)


print('Building fasttext skipgram')
fasttext.skipgram(DATA_FILE, os.path.join(MODELS_DIR, 'fasttext_skipgram'), silent=0)
print('Done with fasttext skipgram')

print('Building fasttext cbow')
fasttext.cbow(DATA_FILE, os.path.join(MODELS_DIR, 'fasttext_cbow'), silent=0)
print('Done with fasttext cbow')

print('Building word2vec skipgram')
Word2Vec(LineSentence(DATA_FILE), size=300, sg=1, workers=-1) \
    .save(os.path.join(MODELS_DIR, 'word2vec_skipgram'))
print('Done with word2vec skipgram')

print('Building word2vec cbow')
Word2Vec(LineSentence(DATA_FILE), size=300, sg=0, workers=-1) \
    .save(os.path.join(MODELS_DIR, 'word2vec_skipgram'))
print('Done with word2vec cbow')
