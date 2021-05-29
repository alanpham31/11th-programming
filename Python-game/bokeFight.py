#Sophia Turner
import time
import random
from main import main
from kennen import Kennen
from belldolpine import Belldolpine
from meisterBeast import MeisterBeast
from bat import Bat
from caterpillar import Caterpillar
from rat import Rat
from player import Player

class BokeFight:
  def fight():
    enemyList = ['bat', 'caterpillar', 'rat'] #finish this
    enemySelect = random.randint(1,len(enemyList))
    enemy = enemyList[enemySelect]
    print('You are facing off with a ', enemy)
    time.sleep(1)
    while(True):
      start,action,attack, = '0','0','0','0'
    while start != 'k' and start != 'b' and start != 'm':
      start = input('Which bokémon would you like to start with?\n[k = Kennen, b = Bell Dolpine, m = Meister beast]\n').lower()
      print('You have chosen ', start, '!')
    while action != 'a' and action !='c' and action !='r': 
      action = input('Would you like to attack [a] or catch [c] or run [r]\n').lower()
    while attack != 'b' and attack != 's':
      attack = input('Would you like to use your basic attack [b] or your special attack [s]\n')
    #KENNEN
    if start == 'k':
      if action == 'a': 
        if attack == 'b':
          print('You have chosen to attack. Kennen does ', Kennen.basicDamage, 'to the', enemy)
        if attack == 's':
          print('You have chosen to attack. Kennen does ', Kennen.specialDamage, 'to the', enemy)
      elif action == 'c': 
        print('You attempt to capture the ', enemy)
        Player.bokemonCatch
        #break
      elif action == 'r': 
        print('You ran away from the fight.')
    #BELLDOLPINE
    if start == 'b':
      if action == 'a': 
        if attack == 'b':
          print('You have chosen to attack. Belldolpine does ', Belldolpine.basicDamage, 'to the', enemy)
        if attack == 's':
          print('You have chosen to attack. Belldolpine does ', Belldolpine.specialDamage, 'to the', enemy)
      elif action == 'c': 
        print('You attempt to capture the ', enemy)
        Player.bokemonCatch
        #break
      elif action == 'r': 
        print('You ran away from the fight.')
    #MEISTERBEAST
    if start == 'm':
      if action == 'a': 
        if attack == 'b':
          print('You have chosen to attack. Meister Beast does ', MeisterBeast.basicDamage, 'to the', enemy)
        if attack == 's':
          print('You have chosen to attack. Meister Beast does ', MeisterBeast.specialDamage, 'to the', enemy)
      elif action == 'c': 
        print('You attempt to capture the ', enemy)
        Player.bokemonCatch
        #break
      elif action == 'r': 
        print('You ran away from the fight.')