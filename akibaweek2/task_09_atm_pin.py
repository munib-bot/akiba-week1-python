pin = 1234
i = 0
count = 3
for i in range(1,4):
    num= int(input( "enter your pin "))
    if num == pin:
        print(" correct pin ")
        break
    else:
     count -=1
     print("incorrect pin")
    print("Attempts remaining",count)
