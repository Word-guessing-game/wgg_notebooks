''' The simple game model - word similarity '''

import random
import re
from itertools import product
from nltk.corpus import wordnet as wn
from nltk.corpus import reader as wn_reader
from api.models.word_corpus import WordCorpus

NOUN = 'n'

class Nltk(WordCorpus):
  ''' This class implements find similarity word for another '''
  def __init__(self):
    self.corpus_size = len([*wn.words()])
    self.nouns_with_distance = None
    return

  def prepare(self, target_word: str):
    ''' Compare all other words in corpus with target and calculate min and max distance '''
    self.minimal_distance = 1.0
    self.maximal_distance = 0
    self.best_word = None
    self.worst_word = None
    target_synset = wn.synsets(target_word)[0]
    if self.nouns_with_distance is None:
      self.nouns_with_distance = []

    for other_word in list(wn.words()):
      if other_word == target_word:
        continue

      other_synset = wn.synsets(other_word)[0]
      part_of_speech = other_synset.pos()
      if self.__is_multipart_word(other_word):
        continue

      if part_of_speech != NOUN:
        continue

      distance = target_synset.wup_similarity(other_synset)
      # Раскомментируй эту строку для отладки
      # print(f'distance between "{target_word}" and "{other_word}" is {distance}')
      if distance > self.maximal_distance:
        self.maximal_distance = distance
        self.worst_word = other_word

      if distance < self.minimal_distance:
        self.minimal_distance = distance
        self.best_word = other_word

      self.nouns_with_distance.append((other_word, distance))

    self.nouns_with_distance = sorted(self.nouns_with_distance, key = lambda x: x[1])
    print(f'for word {target_word} minimal distance is {self.minimal_distance} ({self.best_word}), maximal_distance is {self.maximal_distance} ({self.worst_word})')

  def random_word(self) -> str:
    ''' Returns random word from corpus '''
    while True:
      word = list(wn.words())[random.randint(0, self.corpus_size)]
      if self.__is_multipart_word(word):
        continue

      synset = wn.synsets(word)[0]
      # Для демонстрации процесса подбора слова
      # print(f'{word=}, {synset.pos()=}')
      if synset.pos() == NOUN:
        break

    return word

  # TODO - calculate frequency of use word in language
  def __lemma_frequency(self, synset) -> int:
    '''  '''
    return 0

  def __is_multipart_word(self, word: str) -> bool:
    ''' Check word contains more than one part '''
    return re.search(r'[-_\s]', word)

  def similarity(self, target_word: str, word_attempt: str) -> tuple[str, int]:
    ''' Compare two words and returns their similarity in text sentence '''
    if word_attempt in self.nouns_with_distance:
      similarity = self.nouns_with_distance[word_attempt]
      distance = self.__find_distance(word_attempt)
    else:
      try:
        target_synset = wn.synsets(target_word)[0]
        attempt_synset = wn.synsets(word_attempt)[0]
        similarity = target_synset.wup_similarity(attempt_synset)
        distance = self.__interpolate_distance(similarity)
      except IndexError:
        similarity = 0
        distance = self.corpus_size

    print(f'# debug: {similarity=}')

    return (self._similarity_degree(similarity), distance)

  def __find_distance(self, word: str) -> int:
    ''' Find distance by precalculated list of words with their distance to target '''
    for index, tuple in enumerate(self.nouns_with_distance):
      if tuple[0] == word:
        break

    return index

  def __interpolate_distance(self, similarity: float) -> int:
    ''' Returns integer value representing the number of more similar words than this '''
    return int((1 - similarity) * self.corpus_size)
