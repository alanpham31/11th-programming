import time
from boke_ascii_art import art
from player import Player 
from kennen import Kennen
from belldolpine import Belldolpine
from meisterBeast import MeisterBeast
#from bokeFight import BokeFight
from paintbrushTown import PaintbrushTown
#city 2
#city 3
from cave import Cave

def main():

  print ("Hello there! Welcome to the world of Bokémon! My name is Cottonwood! People call me the bokémon Professor! This world is inhabited by creatures called Bokémon! For some people, Bokémon are pets. Others use them for fights. Myself...I study Bokémon as a profession.\n")
  time.sleep(4)
  PK = input ("What is your name?\n")
  print("So they call you",PK,"\n")
  #PK = Player #MIGHT NOT WORK, FIX IT IF NEED TO
  time.sleep(1)
  print("What an interesting  name")
  time.sleep(3)
  print("Im so sorry to jump right into it but your parents have disapeared\nthey were working at their laboratory at the dig site right out of town")
  time.sleep(4)
  print(" you see,")
  time.sleep(2)
  print("I tried to warn them that it was a bad idea to be working that late at night but they insisted")
  time.sleep(3)
  print("I am going to send you out on a journey to defeat all 3 collesseums in this region, the Kantob region")
  time.sleep(2)
  print("You will catch bokémon and train them to battle the collisseum leaders to get badges")
  time.sleep(2)
  print("once you get all 3 colliseum badges I will feel confident in sending you to the dig site to look for you parents")
  time.sleep(3)
  print("I have 3 bokémon and you can choose one of these bokémon as your compaion")
  print('you will also run into other bokémon on your journey.\n sadly you can only carry 3 bokémon at a time')
  time.sleep(2)
  print("so you will send the rest back to me")
  time.sleep(2)
  
  #choosing starter bokemon

  print('The time has come')
  time.sleep(4)
  print('Which bokémon do you want')
  print('you will type the corresponding letter ')
  print('CHOOSE YOUR BOKEMON')
  starter = input('(A): Kennen, the electic mouse bokémon\n(B): Belldolpine, the E-dolphin time bokémon\n(C): Meister beast, The money bokémon\n')
  while starter not in ("A","a","B","b","C","c"):
    starter = input('please input: A,B, or C\n')

  if starter == 'A' or starter == 'a':
    boke1 = Kennen()
  elif starter == 'B' or starter == 'b':
    boke1 = Belldolpine()
  elif starter == 'C' or starter == 'c':
    boke1 = MeisterBeast()

  print('I see you caught',boke1,'\n well then I will see you on your journey')
  time.sleep(3)
  print(chr(27) + "[2J")
  journey1()
  PK.travel()
  journey1()

def journey1(): 
  print('Professor Cottonwood leads you out of your small town \nand points you in the direction of the next town, Paintbrush Town')
  time.sleep(2)
  print('you have a chance to catch pokemon on your journey\nbut remeber you may only carry 3 at a time')
  time.sleep(1) 


main()