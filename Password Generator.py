#Find out Max number in a list
student_scores=[12,344,578,908,378,289,984]
print(max(student_scores))
new_hero_score=0
for score in student_scores:
    if score>new_hero_score:
        new_hero_score=score
print(new_hero_score)

#The Gauss Challenge
sum_total=0
for number in range(1,101):
    sum_total+=number
print(sum_total)

#Exercise:
for number in range(1,101):
    if number%15 == 0:
        print("FizzBuzz")
    elif number%5==0:
        print("Buzz")
    elif number%3==0:
        print("Fizz")
    else:
        print(number)

#Password Generator
import random
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','v','w','x','y','z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','@','#','$','%','^','&','*','+']

print("Welcome to PyPassword Generator!")
nr_letter=int(input("How many letters would you like in the password?\n"))
nr_symbol=int(input("How many symbols would you like?\n"))
nr_number=int(input("How many numbers would you like?\n"))


#Easy Level
password=""
for i in range(0,nr_letter):
    password += random.choice(letters)
for i in range(0,nr_symbol):
    password += random.choice(symbols)
for i in range(0,nr_number):
    password += random.choice(numbers)
print(password)

#Hard level
password_list= []
for i in range(0,nr_letter):
    password_list.append(random.choice(letters))
for i in range(0,nr_symbol):
    password_list.append(random.choice(symbols))
for i in range(0,nr_number):
    password_list.append(random.choice(numbers))
random.shuffle(password_list)

password=""
for char in password_list:
    password += char
print(f"Your password is: {password}")
