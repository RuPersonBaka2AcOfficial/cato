import os

class Sys():
  def clr():
    if os.name == 'nt':
      os.system('cls')
    else:
      os.system('clear')
