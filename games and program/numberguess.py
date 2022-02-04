n = 30
guesses = 1
print("Your guess is limited to 10 times")
while(guesses<=10):
    x = int(input("Enter the Number\n"))
    guesses = guesses+1
    if x>30:
        print("Your number is too high!")
    elif x<30:
        print("Your number is too low!")
    elif x==30:
        print("You entered Correct number\n")
        break
    else:
        print("Number",10-guesses)
        print("Game over")

    



    