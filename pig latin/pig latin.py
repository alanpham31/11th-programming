from itertools import zip_longest

print ("English to Pig Latin converter!")
t = int(0)

def again():
    print("\nWould you like translate another word?")

    s = input("[y/n] ")

    if s == "y":
      print("\n")
      converter()
    elif s == "n":
      return
    else:
      print("Please enter 'y' for yes or 'n' for no.")
      again()

def converter():
   global t
   t += 1
   
   time_one()
   word = input("Please enter one word at a time for maximum accuracy. Enter word: ")
   b = word[::-1]
   list_vowels = []
   list_consonants = []
   final_list = []
   string = ''
   vowels = ['a', 'e','i','o','u']
   for i in b:
      if i in vowels:
         list_vowels.append(i)
      elif i not in vowels:
         list_consonants.append(i)
   print(''.join(map(lambda x: x[0] + x[1], zip_longest(list_vowels, list_consonants, fillvalue='')))+"ay")
   again()
   
def time_one():
   if t == 1:
        print ("Try it out with your first and last name!\n")
   else:
        return
converter()
