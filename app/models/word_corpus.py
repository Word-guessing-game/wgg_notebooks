''' The simple game model - word similarity '''

import random
import gensim.downloader as api
from gensim.models.word2vec import Word2Vec

class WordCorpus:
  ''' This class implements find similarity word for another '''
  SIMILARITY_DEGREES = (
    (0, 'not similar'),
    (0.4, 'not very similar'),
    (0.5, 'rather unlike'),
    (0.6, 'slighty similar to'),
    (0.7, 'a bit like'),
    (0.8, 'look like'),
    (0.9, 'very similar to'),
    (1.0, 'Congratulations! You are guess!'))

  def __init__(self, model_name):
    self.model_name = model_name
    self._load_model()

  def similar_words(self, word: str) -> list[tuple[str, float]]:
    ''' Returns list of tuples, each tuple contains a similar word and similarity ckoefficient '''
    try:
      similar_words = self.model.wv.most_similar(word.lower())
    except KeyError:
      similar_words = [(word, 1)]

    return similar_words

  def best_similar_word(self, word: str) -> tuple[str, str]:
    ''' Get most similar word from others by maximum koeficient '''
    variants = self.similar_words(word)
    variant = sorted(variants, key = lambda x: x[1], reverse = True)[0]
    similarity_degree = self._similarity_degree(variant[1])
    return (variant[0], similarity_degree)

  def similarity(self, word: str, another_word: str) -> tuple[str, int]:
    ''' Compare two words and returns their similarity in text sentence '''
    try:
      similarity = self.model.wv.similarity(word, another_word)
    except KeyError:
      similarity = 0
    except UnicodeDecodeError:
      similarity = 0

    return [self._similarity_degree(similarity), self.interpolate_index(word, another_word)]

  def interpolate_index(self, target_word: str, word_attempt: str) -> int:
    ''' Returns a index in filtered by less similarity dictionary of corpus words '''
    try:
      most_similar_words_count = len(self.model.wv.words_closer_than(target_word, word_attempt))
    except KeyError:
      most_similar_words_count = self.corpus_length

    return most_similar_words_count

  def print_similar_words(self, words_list: list[tuple]):
    ''' Output to console list of similar words with similarity koefficient '''
    for word_tuple in words_list:
      print(f'word: {word_tuple[0]}, similarity: {word_tuple[1]}')

  def random_word(self) -> str:
    ''' Returns random word from corpus '''
    words = [*self.model.wv.key_to_index.keys()]
    return words[random.randint(0, len(words))]

  @property
  def corpus_length(self) -> int:
    ''' Return size of word corpus '''
    return len(self.model.wv)

  def _load_model(self):
    ''' Download desired and load it to memory '''
    print(f'download model {self.model_name}, wait, please...')
    corpus = api.load(self.model_name)
    print(f'model downloaded, load it into memory...')
    self.model = Word2Vec(corpus)
    print(f'model loaded. Thank you for patience!')

  def _similarity_degree(self, similarity: float) -> str:
    ''' Returns a human-like degree of similarity by similarity koefficient '''
    return list(filter(lambda x: x[0] >= similarity, WordCorpus.SIMILARITY_DEGREES))[0][1]
