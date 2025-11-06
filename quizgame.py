print("QUIZ GAME!")
score = 0
playing = input("Do you want to play? ")
if playing.lower() != "yes":
    quit()

print("Okay! Let's play:)")

answer = input("Whate does CPU stnad for? ")

if answer.lower() == "central processing unit":
    print('Correct!')
    score += 1
elif answer.lower() == "centralprocessingunit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!!")

print("final score :"+str(score))

