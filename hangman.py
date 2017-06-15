from __future__ import print_function
words= ("Tree", "Virus", "Hangman", "Ebola", "Fun")
import numpy
word=(numpy.random.choice(words))
print(len(word))
letter = ""
while len(letter)!= 1:
        letter=raw_input("Please enter a single letter to guess the word!")
print(letter)