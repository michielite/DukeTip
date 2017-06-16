from __future__ import print_function
words= ("Tree", "Virus", "Hangman", "Ebola", "Fun")
man1='''
import numpy
print(man1)
word = (numpy.random.choice(words))
s = word
print(len(word))
WRONG=()
numberWrong=len(WRONG)
while True:
    letter = raw_input("Please enter a single letter to guess the word!")
    klo= letter
    while len(letter) == 1:
        if klo in s:
            print("correct")
            break
        else:
            print("Letter" letter "was incorrect")
            break
    def printHangman(numberWrong):
        if numberWrong >=1:
            print("head")
        else:

            if numberWrong >= 2:
                print("body")
            else:
                if numberWrong >= 3:
                    print("arms")
                else:
                    print("You are correct")

