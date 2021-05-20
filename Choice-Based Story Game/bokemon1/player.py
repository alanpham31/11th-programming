#Sophia Turner
import random
class Player:
  #member variables
  inventory = 1
  bokeSqares = 10
  #constructor

  #methods
  def travel(self):
    bokemonFind = int(random(1,3))
    if(bokemonFind == 1):
      print('As you walk, you find a wild bokémon,')
    elif(bokemonFind == 2):
      print()
    elif(bokemonFind == 3):
      print()
  def catch(self):
    if(self.inventory >= 3 or self.bokeSquares <= 0):
      print()
    bokemonCatch = int(random(1,3))
    if(bokemonCatch == 3):
      print()
    elif (self.inventory < 3):
      self.inventory += 1
      print('Bokémon captured!\nYou have ', self.inventory, 'Bokémon in your inventory')