print("Hello, welcome to my game!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay lets play")
score = 0

answer = input("what color is the sky during the day? ")
if answer.lower() == "blue":
    print("correct")
    score += 1
else:
    print("wrong")

answer = input("how many days are in a week? ")
if answer.lower() == "7":
    print("correct")
    score += 1
else:
    print("wrong")

answer = input("what color is a rose? ")
if answer.lower() == "red":
    print("correct")
    score += 1
else:
    print("wrong")

print("Final score is " + str(score))

    