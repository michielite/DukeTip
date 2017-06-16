from __future__ import print_function
words= ("Tree", "Virus", "Hangman", "Ebola", "Fun")
man='''
   +---+
   |   |
       |
       |
       |
       |
========''',
'''
   +---+
   |   |
   O   |
   |   |
       |
       |
=======''',
'''
   +---+
   |   |
   O   |
  /|\  |
       |
       |
=======''',
'''
   +---+
   |   |
   O   |
  /|\  |
  /    |
       |
=======''',
'''
   +---+
   |   |
   O   |
  /|\  |
  / \  |
       |
======='''
import numpy
word = (numpy.random.choice(words))
s = word
print(len(word))
while True:
    WRONG=()
    numberWrong=len(WRONG)
    if numberWrong == 0:
        print(man[0])
        break
    else:
        if numberWrong == 1:
            print(man[1])
        else:
            if numberWrong >= 3:
                print("arms")
            else:
                print("You are Dead")
letter = raw_input("Please enter a single letter to guess the word!")
klo= letter
while len(letter) == 1:
    if klo in s:
        print("correct")
    else:
        print("Letter was incorrect")
