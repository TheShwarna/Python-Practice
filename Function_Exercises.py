#Functions and variables
def greet():
    print("Hello World")
    print("Happy day!")
    print("Have a nice day!")

greet()
#
# #Function with a variable input
def greet_with_name(name):
    print(f"Hello {name}")
    print(f"Happy day {name}!")
    print(f"Have a nice day {name}!")
greet_with_name("David")

def life_in_weeks(age):
    x=int((90-age)*52)
    print(f"You have {x} weeks left.")
life_in_weeks(56)

#True Love counter

def calculate_love_score(name1,name2):
    score1 = 0
    score2 = 0
    for letter in name1:
        if letter == "t":
            score1 += 1
        elif letter == "r":
            score1 += 1
        elif letter == "u":
            score1 += 1
        elif letter == "e":
            score1 += 1
            score2 += 1
        elif letter == "l":
            score2 += 1
        elif letter == "o":
            score2 += 1
        elif letter == "v":
            score2 += 1

    for letter in name2:
        if letter == "t":
            score1 += 1
        elif letter == "r":
            score1 += 1
        elif letter == "u":
            score1 += 1
        elif letter == "e":
            score1 += 1
            score2 += 1
        elif letter == "l":
            score2 += 1
        elif letter == "o":
            score2 += 1
        elif letter == "v":
            score2 += 1
    print(str(score1)+str(score2))
calculate_love_score("Angela Yu" ,"Jack Bauer")
