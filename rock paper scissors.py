import time
import random

number = random.randint(0, 4)
score_y = 0
score_x = 0




#computer player 

def game(number):
    if number == 1:
        x = "rock"
        print("")
        print("computer:")
        print("rock")
        print("""                 /////
             //////////
           /////////////
            //////////
             ///////""")
        return x
    if number == 2:
        x = "paper"
        print("")
        print("computer:")
        print("paper")
        print("""                         ---------
                         ---------
                         ---------
                         ---------
                         ---------""")
        return x
    if number == 3:
        x = "scissors"
        print("")
        print("computer:")
        print("scissors")
        print("""    /
                   0/
                   0\
                     \ """)
        return x
    
    
#player input  
    
    
def your_play(input):
    if input == 1:
        y = "rock"
        print("your play:")
        print("rock")
        print("""                 /////
             //////////
           /////////////
            //////////
             ///////""")
        return y 
    if input == 2:
        print("your play:")
        print("paper")
        y = "paper"
        print("""                         ---------
                         ---------
                         ---------
                         ---------
                         ---------""")
        return y
    if input == 3:
        print("your play:")
        print("scissors")
        y = "scissors"
        print("""    /
                   0/
                   0\
                     \ """)
        return y
  
  




#judge of who wins the game 
  
def judge(x, y):
    global score_y
    global score_x
    if x == y:
        print("DRAW")
        print("\(-_-)/")
    if x == "rock" and y == "paper":
        score_y += 1 
        print("YOU WIN :)")
        return score_y
    if x == "rock" and y == "scissors":
        score_x += 1
        print("YOU LOOSE :(")
        return score_x
    if x == "paper" and y == "scissors":
        score_y += 1
        print("YOU WIN :)")
        return score_y
    if x =="paper" and y == "rock":
        score_x += 1
        print("YOU LOOSE :(")
        return score_x



#functions -----


print("SCORE")
print(score_x, score_y)
print("")
        
play = int(input("------->"))


y = your_play(play)
x = game(number)
judge(x, y)




print("SCORE")
print(score_x, score_y)
print("")
        
play = int(input("------->"))


y = your_play(play)
x = game(number)
judge(x, y)


   
   

