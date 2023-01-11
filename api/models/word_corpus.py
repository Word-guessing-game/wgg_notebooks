''' The simple game model - word similarity '''

from abc import ABCMeta, abstractmethod
import pdb

class WordCorpus(metaclass = ABCMeta):
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

  @abstractmethod
  def random_word(self) -> str:
    ''' Returns random word from corpus '''
    return

  @abstractmethod
  def similarity(self, target_word: str, word_attempt: str) -> tuple[str, int]:
    ''' Compare two words and returns their similarity in text sentence '''
    return

  def _similarity_degree(self, similarity: float) -> str:
    ''' Returns a human-like degree of similarity by similarity koefficient '''
    return list(filter(lambda x: x[0] <= similarity, WordCorpus.SIMILARITY_DEGREES))[-1][1]
