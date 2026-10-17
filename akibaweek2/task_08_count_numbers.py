num = int(input("enter the number to check if it's even, odd "))
odd = 0
even = 0
sum = 0 
for i in range(1,num+1):
    if i%2==0:
     even +=1
    else:
      odd +=1
      sum += num
print("the number of the even is",even)
print("the number of the odd is",odd)
print("the sum of the number is",sum)