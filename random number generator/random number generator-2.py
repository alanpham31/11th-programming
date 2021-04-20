import random
i=random.randint(0,100)
t = int(0)
d = int(0)
print("Guess the Number!!")
def give_hint():
  hint = abs(int(round(i-x,-1)))
  if t%4 != 0:
    return
  if hint < 10:
    print("You are really close !\n")
  elif hint >= 10:
    print("It looks like you are having some trouble! Here's a hint: You are roughly",hint,"away!\n")

def play_again():
    global t
    global d
    print("\nWould you like to play again?")
    s = input("[y/n] ")
    d += 1
    if s == "y":
        print("\n")
        check_number()
    elif s == "n":
        print("You played", d, "rounds.")
        print("\nGoodbye, come back again later!")
        return
    else:
        print("Please enter 'y' for yes or 'n' for no.")
        play_again()

def check_number():
  global x
  global t
  global i
  global s
  t += 1
  print(i)
  try:
    x = int(input("Enter a positive number between 0 and 100: "))
  except:
    print("\nPlease make sure you have entered a number and that it also has no decimals\n")
    check_number()  
  if x > i:
      print("\nYou guessed:",x,"That number is too high. Try again!\n")
      give_hint()
      check_number()
  elif x < i:
      print("\nYou guessed:",x,"That number is too low. Try again!\n")
      give_hint()
      check_number()
  elif x == i:
      print("\nYou guessed:",x,"That was the right answer. Good Job! That took you",t,"attempts.")
      i=random.randint(0,100)
      t = int(0)
      play_again()
  else:
      print("Please enter a Number")
      check_number()

check_number()
