# Cmd + / makes code comment
# Tip Generator
Bill = int(input("Welcome to the tip calculator!\nWhats the bill amount?"))
Tip = int(input("How much tip would you like? 10, 15 or 25"))
People = int(input("How many people would like to split with?"))
Split = round(Bill*(1+Tip/100)/People,2)
print(f"Each person has to pay $ {Split}")
