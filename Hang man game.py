#Hang Man
import random
import Words
from hangman_art import HANGMANPICS,logo
rand_word= random.choice(Words.word_list)
print(logo[0])
word_blank = "_"*len(rand_word)
print(word_blank)

correct_guess=[]
all_guess=[]
game_over = False
life = 6

while not game_over:
    guess= input("Enter your guess: ").lower()
    word_blank1 = ""
    if guess in all_guess:
        print(f"You've already guessed {guess} letter. Try again")
        word_blank1 = word_blank
    else:
        all_guess.append(guess)
        for letter in rand_word:
            if guess == letter:
                word_blank1+= letter
                correct_guess.append(guess)
            elif letter in correct_guess:
                word_blank1 += letter
            else:
                word_blank1+= "_"
        if guess not in correct_guess:
            life -= 1
            print(f"The letter {guess} is not in the word. You lose a life!")
            if life == 0:
                game_over = True
    if  "_" not in word_blank1:
        print("You win!")
        game_over = True

    print(word_blank1)
    if  life==6:
        print(HANGMANPICS[0])
        print("***YOU HAVE 6/6 LIVES LEFT***")
    elif life==5:
        print(HANGMANPICS[1])
        print("***YOU HAVE 5/6 LIVES LEFT***")
    elif life==4:
        print(HANGMANPICS[2])
        print("***YOU HAVE 4/6 LIVES LEFT***")
    elif life==3:
        print(HANGMANPICS[3])
        print("***YOU HAVE 3/6 LIVES LEFT***")
    elif life==2:
        print(HANGMANPICS[4])
        print("***YOU HAVE 2/6 LIVES LEFT***")
    elif life==1:
        print(HANGMANPICS[5])
        print("***YOU HAVE 1/6 LIVES LEFT***")
    else:
        print(HANGMANPICS[6])
        print("Game over. You lose!\nThe word was: " + rand_word)
