#alan pham
import random
class Bat:
  def work():
  #member variables
    
    global hp
    global exp
    global basicDamage
    global specialDamage

    hp = 8
    exp

    basicDamage = random.randint(3,5)
    specialDamage = random.randint(8,10)

  #constructor

  #methods
  def __init__(self, basicAttack, specialAttack, dropExp):
    self.basicAttack = attack
    self.specialAttack2 = attack
  def basicAttack(self):
    damage = self.basicDamage
    print('You did ', self.basicDamage, ' damage!')
  def specialAttack1(self):
    damage = self.specialDamage
    print('You did ', self.specialDamage, ' Electric damage!')
  def dropExp(self):
    damage = ('Bat dropped' ,' exp!')