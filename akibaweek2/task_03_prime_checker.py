num = int(input("Enter a number to check if it is prime: "))
if num <= 1:
    print(f"{num} is not a prime number")
else:
    for i in range(2, num):
        if num % i == 0:
            print(f"{num} is not a prime number")
            break
    else:
        print(f"{num} is a prime number")
        # EXPLANATION:
# Factors of a number always come in pairs (for example, factors of 36 are 2x18, 3x12, 4x9, 6x6).
# In any factor pair (a * b = n), at least one factor must be less than or equal to sqrt(n).
# If 'n' had a divisor greater than sqrt(n), its matching pair would have already been found 
# below or at sqrt(n). If no divisor is found up to sqrt(n), the number has no factors other 
# than 1 and itself, making it prime.