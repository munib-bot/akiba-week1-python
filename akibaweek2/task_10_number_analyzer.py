num = int(input("How many numbers do you want to enter? "))
total = 0
odd = 0
even = 0
largest = None
smallest = None
for i in range(num):
    number = int(input("Enter a number: "))
    
    if number % 2 == 0:
        even += 1
    else:
        odd += 1

    total += number

    if largest is None or number > largest:
        largest = number

    if smallest is None or number < smallest:
        smallest = number

if num > 0:
    average = total / num

    print("Number of odd numbers is:", odd)
    print("Number of even numbers is:", even)
    print("Sum is:", total)
    print("Average is:", average)
    print("Largest number is:", largest)
    print("Smallest number is:", smallest)
else:
    print("Please enter a number greater than zero.")