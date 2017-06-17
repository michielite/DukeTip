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
def printBlanks(word, correct):
    # Set solved equal to true (innocent until proven guilty)
    # Loop over each letter in the word  for l in word:
    l = l.lower() # not required but nice to have
    # Check if that letter is in the list of correct letters
    if klo in correct: # Remove "False" and replace it with the appropriate condition
        # If it is, print the letter and a space
        print(klo)
        print(" ")
    else:
        print("_ ")
        # If it isn't, print an underscore and a space
        # Also, set solved equal to False
    print();
    print();
    return solved

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
    if klo in s:
        correct.append(klo)
        print("correct")
    else:
        print("Letter was incorrect")
        WRONG.append(["1"])