import random

#print(random.randint(1,100))

#l=[1,2,3,"yash","mordhara"]
#print(random.choice(l))

num=random.randint(1,20)

while True:
    guess=int(input("Guess a number between 1 to 20 : "))
    if guess==num:
        print("you guessed correct number...")
        break
    elif guess>num:
        print("you guessed A greater number...")
    elif guess<num:
        print("you guessed A smaller number...")
