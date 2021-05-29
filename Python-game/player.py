#Sophia Turner
import random
class Player:
  #member variables
  inventory = 1
  bokeSqares = 9999999999
  #constructor

  #methods
  def travel():
    bokemonFind = random.randint(1,3)
    if(bokemonFind == 1):
      print('1place')
    elif(bokemonFind == 2):
      print('2place')
    elif(bokemonFind == 3):
      print('3place')
  def catch(self):
    if(self.inventory >= 3 or self.bokeSquares <= 0):
      print()
    bokemonCatch = int(random.uniform(1,3))
    if(bokemonCatch == 3):
      print()
    elif (self.inventory < 3):
      self.inventory += 1
      print('Bokémon captured!\nYou have ', self.inventory, 'Bokémon in your inventory')
