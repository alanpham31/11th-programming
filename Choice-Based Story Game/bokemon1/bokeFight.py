#Sophia Turner
import time
from main import main

class BokeFight:
  print('You are facing off with a ___')
  time.sleep(1)
  print('Which bokémon would you like to start with?')
  start = input('A: ', main.boke1,'B: ')
  if(start == 'A' or start == 'a'):
    print()
  time.sleep(3)
  print('FIGHT!')
  time.sleep(1)