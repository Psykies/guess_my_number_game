#for genearating a random number
from random import *
guess_num = (randint(1, 100))
print ("I ma thining of a number from  1 to 100. can you guess which is it ")
mode = input("enter whiich mode you want ot chosse easy or hard")
if mode == "easy":
    print ("you get 10 chance to guess")
    attemp = 10
    
    while attemp != 0 :
        
        guess = int(input("Guess the number "))
        if guess ==  guess_num:
            print ("you got it right")
            break
        elif (guess >  guess_num):
            print ("you guess is higher than mine")
        else:
            print ("you guess is lower than mine")
        
        if attemp == 1:
            print ("your guess are over")
            print(f"my guess was {guess_num}")
        attemp -= 1
        
if mode == "hard":
    print ("you get 5 chance to guess")
    attemp = 5
    
    while attemp != 0 :
        
        guess = int(input("Guess the number "))
        if guess ==  guess_num:
            print ("you got it right")
            break
        elif (guess >  guess_num):
            print ("you guess is higher than mine")
        else:
            print ("you guess is lower than mine")
        if attemp == 1:
            print ("your 5  chance to guess is finished")
            print(f"my guess was {guess_num}")
        attemp -= 1
    

        