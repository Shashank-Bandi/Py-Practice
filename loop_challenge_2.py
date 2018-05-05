import random
#The program should  let the player know whether to guess higher or lower,
# and should print a message if lower or higher. IF the guess is correct terminate the program
# as an optional input = 0 should terminate the program
highest = random.randint(0,1000)
answer = random.randint(1,highest)
guess = int(input("Please guess a number between 1 and {}:".format(highest)))
ctr = int()
total = 10
while guess!=answer:
    if guess<answer:
        guess=int(input("Please guess a higher value:"))
    else:
        guess=int(input("Please guess a lower value:"))
    
    if guess == answer:
        print("Well Done!, You`ve guessed correctly:",answer)
    else:
        print("Sorry, Incorrect guess")
    ctr = ctr +1
    count = total-ctr
    print("You have {} tries left".format(count))
    if count==0:
        print("Sorry, out of tries, Better luck next time :)")
        break
else:
    print("Thanks for playing:)")
    
