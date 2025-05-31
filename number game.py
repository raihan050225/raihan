import time
import random
name1=input("player 1 enter your name ")
name2=input("player 2 enter your name")
print("hello {} and {}".format(name1,name2))
print("     RULES OF THE GAME     ")
print("the system will have 5 numbers you both get 3 chances to get the answers correctly")
print("for each answer you get 1 point and lose a point for wrong answer")
print("            LETS GO       ")

num=[]
while(len(num)!=5):
    d=random.randint(1,11)
    if(d in num):
        continue
    else:
      num.append(d)
player1=[]
player2=[]
wrong=[]
s1=0
s2=0
for i in range(3):
    print("{}enter your guess".format(name1))
    ans=int(input())
    if(ans in player1 or ans  in player2 or ans in wrong):
        print("already taken guess another number:")
        ans=int(input())
        if(ans not in player1 and ans not in player2 and ans in num):
            print("correct")
            player2.append(ans)
            s2=s2+1
        elif(ans not in num):
         print("wrong)")
         player1.append(ans)
         wrong.append(ans)
         s1=s1-1

    
    
    elif(ans not in num):
        print("wrong)")
        player1.append(ans)
        wrong.append(ans)
        s1=s1-1
        
    elif(ans not in player1 and ans not in player2 and ans in num):
        print("correct")
        player1.append(ans)
        s1=s1+1
   
        
    print("{}enter your guess".format(name2))
    ans=int(input())
        
        
    if(ans in player1 or ans  in player2 or ans in wrong):
        print("already taken guess another number:")
        ans=int(input())
        if(ans not in player1 and ans not in player2 and ans in num):
           print("correct")
           player2.append(ans)
           s2=s2+1
        elif(ans not in num):
         print("wrong)")
         player2.append(ans)
         wrong.append(ans)
         s1=s1-1
    
    elif(ans not in num):
        print("wrong)")
        player2.append(ans)
        wrong.append(ans)
        s2=s2-1  
          
           
    elif(ans not in player1 and ans not in player2 and ans in num):
        print("correct")
        player2.append(ans)
        s2=s2+1
        
print("game has been completed")
time.sleep(2)
print(" the results are")
print("{} predicted {} ".format(name1,player1))
print("{} predicted {} ".format(name2,player2))
time.sleep(2)
print("{} score is {} ".format(name2,s2))
print("{} score is {} ".format(name1,s1))
time.sleep(2)

if(s1>s2):
    print("{} is the winner".format(name1))
elif(s1==s2):
    print("score is equal draw")
else:
    print("{} is the winner".format(name2))


