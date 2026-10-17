secret = 9
count = 0
while count<5:
    guess = int(input("Guess the number "))
    count += 1
    if secret == guess:
        print("congratulation you get the answer ")
    elif guess > secret:
        print("too high")
    else:
        print("too low")
if guess != secret:
 print("game over the secret number is",secret)