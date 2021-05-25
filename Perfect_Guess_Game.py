# -*- coding: utf-8 -*-
"""
Created on Sun May 23 19:44:11 2021

@author: RUDRANIL
"""

import random as rn
#from IPython.display import clear_output    only for jupyter

#computer generated number
x=rn.randint(0,10000)
name = input('Enter your name:')
counter=0
high=9
print("Guess the number between 0-10000\n")
while True:
    #user input
    y=int(input())
    counter+=1
    if x == y:
        print("{}'s guess of {} is correct. It took you {} guesses".format(name,y,counter))
        if counter < high:
            high=counter
        print("The high Score is {}".format(high))
        break
    elif x > y:
        #clear_output()  only  for jupyter use instead of next line
        print('\n'*100)
        print('Enter a larger number than {}:'.format(y))
    elif x < y:
        #clear_output()   only for jupyter use instead of next line
        print('\n'*100)
        print('Enter a smaller number than {}:'.format(y))