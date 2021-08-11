#Guess the number by python

import random
t=random.randint(0,9)
print("welcome to NUMBER GUESS GAME")
print("enter your number in the range of 0-9")
n=int(input())
a=1
while 1>0:
       if t == n:
           print("you guessed the number with try = ",a)
           a=a+1
           break
       elif(n<t):
           print("your guess is low,enter another number")
           n=int(input())
           a=a+1
       elif(n>t):
           print("your guess is high,enter another number")
           n = int(input())
           a=a+1


