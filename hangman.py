from __future__ import print_function
words= ("Tree", "Virus", "Hangman", "Ebola", "Fun")
import numpy
word=(numpy.random.choice(words))
s=word
print(len(word))
letter=raw_input("Please enter a single letter to guess the word!")
letter = ""
letter=y
while len(letter)!= 1:
    if letter in word:
        print(y)
        break
    else:
        print("Letter was incorrect")
        break
