''' The simple game model - word similarity '''

import random
import gensim.downloader as api
from gensim.models.word2vec import Word2Vec
from app.models.nlp.word_corpus import WordCorpus

class Gensim(WordCorpus):
  ''' This class implements find similarity word for another '''
  def __init__(self):
    self.model_name = 'text8'
    self.__load_model()

  def similarity(self, target_word: str, word_attempt: str) -> tuple[str, int]:
    ''' Compare two words and returns their similarity in text sentence '''
    try:
      similarity = self.model.wv.similarity(target_word, word_attempt)
    except KeyError:
      similarity = 0
    except UnicodeDecodeError:
      similarity = 0

    return [self._similarity_degree(similarity), self.__interpolate_index(word, word_attempt)]

  def __interpolate_index(self, target_word: str, word_attempt: str) -> int:
    ''' Returns a index in filtered by less similarity dictionary of corpus words '''
    try:
      most_similar_words_count = len(self.model.wv.words_closer_than(target_word, word_attempt))
    except KeyError:
      most_similar_words_count = self.__corpus_length

    return most_similar_words_count

  def random_word(self) -> str:
    ''' Returns random word from corpus '''
    words = [*self.model.wv.key_to_index.keys()]
    return words[random.randint(0, len(words))]

  @property
  def __corpus_length(self) -> int:
    ''' Return size of word corpus '''
    return len(self.model.wv)

  def __load_model(self):
    ''' Download desired and load it to memory '''
    print(f'download model {self.model_name}, wait, please...')
    corpus = api.load(self.model_name)
    print(f'model downloaded, load it into memory...')
    self.model = Word2Vec(corpus)
    print(f'model loaded. Thank you for patience!')
