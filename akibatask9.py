exchange_rate  = 150 
amount_in_usd = int(input("what is your amount in USD ? "))
amount_in_etb = amount_in_usd * exchange_rate
print("=============================================")
print(  " CURRENCY EXCHANGE")
print("=============================================")
print(f" USD Amount : {amount_in_usd}")
print("                          ")
print(f"exchange rate : 1 USD = {exchange_rate} ETB")
print("                          ")
print(f"ETB Amount : {amount_in_etb} ETB")
print("=============================================")