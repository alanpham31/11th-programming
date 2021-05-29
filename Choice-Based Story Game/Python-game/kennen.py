#Sophia Turner
import random
import time
class Kennen:
  #member variables
  hp = 10
  exp = 0
  basicDamage = random.randint(7,9)
  specialDamage = random.randint(11,13)
  hpRegain = random.randint(3,5)
  #constructor

  #methods
  def basicAttack(self):
    damage = self.basicDamage
    print('You did ', self.basicDamage, ' damage!')
  def specialAttack2(self):
    damage = self.specialDamage
    print('You did ', self.specialDamage, ' Electric damage!')
  def heal(self):
    regain = self.hpRegain
    print('You regained ', self.hpRegain, ' health!')