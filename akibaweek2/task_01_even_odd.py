number = int(input("Enter a number to check if it is even or odd: "))
if number % 2==0 and number >0:
    print(f"{number} is positive even number")
elif number % 2==0 and number <0:
    print(f"{number} is negative even number")
elif number % 2==1 and number >0:
    print(f"{number} is positive odd number")
elif number % 2==1 and number <0:
    print(f"{number} is negative odd number")
else:
    print(f"{number}  zero  is neither even nor odd")