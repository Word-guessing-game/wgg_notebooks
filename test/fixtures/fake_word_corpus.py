''' Contains fixture for substitute heavyloaded WordCorpus class '''

from app.models.word_corpus import WordCorpus
from test.fixtures.fake_word_corpus.fake_word_2_vec_model import FakeWord2VecModel

class FakeWordCorpus(WordCorpus):
  ''' This fake corpus class omit loading real model for testing purposes '''

  def _load_model(self):
    ''' Download desired and load it to memory '''
    print(f'download model {self.model_name}, wait, please...')
    self.model = FakeWord2VecModel()
    print(f'model loaded. Thank you for patience!')
