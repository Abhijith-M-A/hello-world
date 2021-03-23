import math
import random
import time

print("\n 5 points will be awarded for each right answer. You win the game if you score 60 points")
print("\n If you get 3 wrong answer, You Lose !!")
time.sleep(3)
a = 1
b = 2
c = 3
score = 0
wrong = 0
grr =[]
frr =[]
krr =[]
look = False
took = False
hook = False

def firstinput(x):
    global look
    if(len(grr)>1):
        for i in (1,len(grr)-1):
            if(grr[i-1]==grr[len(grr)-1]):
                
                look = True
    if(look == True):
        print("\nYou already entered this value")
    if(look == False):
        temp1 = x//2
        j = 0
        for i in range(2,temp1+1):
            rem = x%i
            if(rem == 0):
                j = 1
                wrongfun()
                print("\nYour answer is wrong")
                break
        if(j==0):
            print("\nYou scored 5 points")
            scorefun()

def secondinput(y):
    global took
    if(len(frr)>1):
        for i in (1,len(frr)-1):
            if(frr[i-1]==frr[len(frr)-1]):
                
                took = True
    if(took == True):
        print("\nYou already entered this value")
    if(took == False):
        temp2 = math.sqrt(y)
        check = temp2.is_integer()
        if(check == False):
            print("\nYour answer is wrong")
            wrongfun()
        else:
            print("\nYou scored 5 points")
            scorefun()
        

def thirdinput(z):
    global hook
    if(len(krr)>1):
        for i in (1,len(krr)-1):
            if(krr[i-1]==krr[len(krr)-1]):
                
                hook = True
    if(hook == True):
        print("\nYou already entered this value")
    if(hook == False):
        if (z%21 != 0):
            print("\nYour answer is wrong")
            wrongfun()

        if (z%21==0):
            print("\nYou scored 5 points")
            scorefun()

def wrongfun():
    global wrong
    wrong = wrong + 1

def scorefun():
    global score
    score = score + 5
    


while(wrong<3 and score <60):

    list = [1,2,3]
    char = random.choice(list)
    

    if(char == a):
            
        input_first = int(input("\nEnter a prime number: "))
        grr.append(input_first)
        firstinput(input_first)
    if(char == b):        
        input_second = int(input("\nEnter a number which has square root: "))
        frr.append(input_second)
        secondinput(input_second)

    if(char == c):
        input_third = int(input("\nEnter a number divisible by both 3 and 7: "))
        krr.append(input_third)
        thirdinput(input_third)

if(wrong >2):
    print("\nGame over")
    print("\nYour score is", score)

if(score == 60):
    print("\nYou won the game")


    
