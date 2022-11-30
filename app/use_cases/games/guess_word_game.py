''' Contains Guess word game flow '''

from app.use_cases.console_interface import ConsoleInterface

class GuestWordGame:
  def __init__(self, corpus_class):
    self.interface = ConsoleInterface()
    self.word_corpus = corpus_class()
    self.hidden_word = self.word_corpus.random_word()
    print(f'--------------------- debug info: {self.hidden_word=} --------------------------')
    self.word_corpus.prepare(self.hidden_word)

  def run(self):
    ''' Run interactive game in terminal '''
    word = 'I thought of a word. Try to guess it.'
    while True:
      word = self.interface.input_string('Enter a word or empty if you are tired:')
      if word == '':
        break

      similarity_degree, similarity_index = self.word_corpus.similarity(self.hidden_word, word)
      if word == self.hidden_word:
        print(f'{word} is great! {similarity_degree}')
        return

      print(f'{word} is {similarity_degree}, at a distance of {similarity_index} words from the intended word.')

    print(f'Thank you for that game!')
