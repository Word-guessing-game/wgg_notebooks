''' Simulates a real Vector model '''
class FakeWord2VecModel():
  @property
  def wv(self):
    def similarity(word: str, another_word: str) -> float:
      return 0.624

    @property
    def key_to_index():
      def keys() -> dict:
        return ['word1', 'word2', 'word3', 'word4']

    def most_similar(word: str) -> list(tuple[str, float]):
      return [('word5', 0.624)]
