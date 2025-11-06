import random

game = 0
win = 0
print("Let's Play Rock, Scissors, Paper!!!")
running = True;
while running:
    my = input("choose yours(r/s/p) : ")
    pc = random.randint(0,2)
    game += 1
    if pc == 0:
        print("computer chooses Rock.")
        if my == "r":
            print("draw!")
        elif my == "s":
            print("you lose!")
        elif my == "p":
            print("you win!!!")
            win += 1
        else:
            quit()
    if pc == 1:
        print("computer chooses Scissors.")
        if my == "s":
            print("draw!")
        elif my == "p":
            print("you lose!")
        elif my == "r":
            print("you win!!!")
            win += 1
        else:
            quit()
    if pc == 2:
        print("computer chooses Paper.")
        if my == "p":
            print("draw!")
        elif my == "r":
            print("you lose!")
        elif my == "s":
            print("you win!!!")
            win += 1
        else:
            quit()
    print(f"total game : {game}, winning : {win}")
    
    