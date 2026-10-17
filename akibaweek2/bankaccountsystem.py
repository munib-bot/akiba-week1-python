balance = 200
while True:
 print("========== AKIBA BANK ============")
 print("        1.Check Balance")
 print("        2.Deposit Money")
 print("        3.Withdraw Money")
 print("        4. Exit")
 choice = int(input(" choose the correct option "))
 if choice==1:
     print("your balance is",balance)
 elif choice == 2:
         print("deposit money")
         amount = int(input("enter amount "))
         if balance > 0 and amount>0:
          balance += amount
          print("your balance is",balance)
         else:
          print("invalid amount")
 elif choice == 3:
    print("withdraw money") 
    amount = int(input("enter amount "))
    if amount<= 0:
     print("invalid amount")
    elif amount>balance:
     print("insufficient balance")
    else:
     balance -= amount
     print("your new balance is ",balance)
 
 elif choice == 4:
    print("Thank you for using our bank")
    break
 
