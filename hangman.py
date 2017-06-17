from __future__ import print_function
words= ("tree", "virus", "hangman", "ebola", "fun")
man=['''
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
=======''']
import numpy
word = (numpy.random.choice(words))
s = word
WRONG=[]
correct=[]
while True:
    numberWrong = len(WRONG)
    print(man[numberWrong])
    if numberWrong >= 4:
        print("You are Dead! Good Luck Next Time!")
        break
    print(len(word))
    letter=""
    while len(letter)!=1:
        letter = raw_input("Please enter a single letter to guess the word!")
    klo = letter
    while True:
        if klo in s:
            correct.append(klo)
            print("correct")
            break
        else:
            print("Letter was incorrect")
            WRONG.append(["1"])
            break
