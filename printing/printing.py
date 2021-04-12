fo = open("output.txt", "w")
fo.write ("Name: ")
fo.write (input ("What is your name?\n"))
fo.write ("\nGrade: ")
fo.write (input ("What grade are you in?\n"))
fo.write ("\nFriend count: ")
fo.write (input ("How many friends do you have?\n"))
fo.write ("\nBrowser: ")
fo.write (input ("What kind of interenet browser do you use?\n"))
fo.write ("\nGame: ")
fo.write (input ("If you play video games, what games do you play?\n"))
fo.write ("\nStory Type: ")
fo.write (input ("What are your favorite kinds of stories to read? \n"))
fo.write ("\nComputer Type: ")
fo.write (input("What kind of computer do you have? \n"))
fo.write ("\nTrust: ")

def truststring():
    a = int(input("On a scale 1-10, how much do you trust me? \n"))
    if a >= 5:
        print ("Thats amazing, I trust you a lot as well.\n")
        fo.write (str(a))
    elif a < 5:
        print ("That is such a shame, I trusted you so much :/\n")
        fo.write (str(a))
    else:
        print ("Please enter an integer from 1 to 10")
        truststring()

truststring()
fo.write ("\nInstagram @: @")
fo.write (input("What is your instagram username?\n"))
fo.write ("\nFollowers: ")
fo.write (input("How many followers do you have on instagram?\n"))
fo.write ("\nWPM: ")
fo.write (input("How many words can you type per minute?\n"))
print ("Thank you for taking this short quiz!\n")

fo.close()
