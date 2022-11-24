''' Contains console interface helpers '''

class ConsoleInterface:
  ''' Propose console interface helpers '''
  def input_string(self, message: str) -> str:
    print(message)
    word = input()
    return word
