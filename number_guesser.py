import random

random_number = random.randint(0,11)

while True:
    answer = int(input("guess! "))
    if answer > random_number:
        print("less than "+str(answer))
    elif answer < random_number:
        print("bigger than "+str(answer))
    else:
        print("great!!")
        break