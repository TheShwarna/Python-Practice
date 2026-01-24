
# If else statements
height = int(input("What is your height in cms?"))
if height >= 120:
    print("You shall pass")
    age=int(input("What is your age?"))
    if age <= 12:
        bill=5
        print("Adult ticket price is $5")
    elif age <= 18:
        bill=10
        print("Youth ticket price is $10")
    else:
        bill=15
        print("Adult ticket price is $15")
    photo = input("Do you want a photo? Type y if yes, and n if no.")
    if photo == "y":
        bill +=3
    print("Your total bill is $",bill)
else:
    print("You too short for a rollercoaster")

#Odd or Even
num = int(input("Please input the number to check if it is odd or even?"))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# Pizza Bill amount generator
print("Welcome to Python pizza deliveries!")
size=input("Enter the size of the pizza you want: S,M or L")
pepp=input("Do you want pepperoni in your pizza? Y or N")
cheese=input("Do you want extra cheese in your pizza? Y or N")
if size == "S":
    bill= 15
    if pepp == "Y":
        bill += 2
elif size == "M":
    bill=20
    if pepp == "Y":
        bill += 3
elif size == "L":
    bill=25
    if pepp == "Y":
        bill += 3
else:
    size= input("Please enter either S, M or L")
if cheese == "Y":
    bill += 1
print(f"Final bill amount is ${bill}")

# Treasure Hunt
print("Welcome to Py Treasure hunt game!\nYou're stranded in a deserted island.")
A1 =input("Would you go \"left\" or \"right\"?").lower()
if A1 == "left":
    print("Game over")
elif A1 == "right":
    A2= input("You've reached the beach\nWould you \"swim\" or \"wait\"fpr the boat?").lower()
    if A2 == "swim":
        print("Game over")
    elif A2 == "wait":
        A3= input("A boat approaches.\nWould you use the \"blue\", \"yellow\" or \"red\" door?").lower()
        if A3 == "red":
            print("Game over, you were thrown into a room full of fire.")
        elif A3 == "blue":
            print("Game over, you were thrown back into the sea.")
        elif A3 == "yellow":
            print("You've escaped with the treasure.\nYou win!")
        else:
            print("Back to school.")
    else:
        print("Back to school.")
else:
    print("Back to school")

