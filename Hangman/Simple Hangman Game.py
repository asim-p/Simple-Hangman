#Simple Hangman Game
import random

#random list of words
words = ['ice', 'sun', 'kite', 'pencil', 'cloud', 'queen', 'carrot', 'tree', 
 'coffee', 'umbrella', 'phone', 'mountain', 'orange', 'guitar', 'lamp', 
 'yacht', 'yacht', 'kite', 'pencil', 'kite', 'coffee', 'lemon', 'umbrella', 
 'robot', 'robot', 'lemon', 'phone', 'coffee', 'banana', 'phone']

#To print word
def print_word(word):
    i=0
    while (i<len(word)):
        if word[i] in guessed_letters:
            print(word[i],end=" ")
        else:
            print("_",end=" ")
        i+=1

#To check win condition
def win(word):
    i=0
    while(i<len(word)):
        if word[i] not in guessed_letters:
            return False
        i+=1
    return True

#Main program
word = random.choice(words)
guessed_letters = []
lives = 6
while (lives!=0):
    print("__________________________________________________")
    print("Lives =",lives)
    print_word(word)
    guess = input("\nChoose your guess: ")
    if guess not in guessed_letters:
        guessed_letters.append(guess)
        if guess in word:
            print("Good guess!!!")
            if win(word) == True:
                print("__________________________________________________")
                print("The word was",word)
                print("YOU WIN!!!")
                exit(0)
        else:
            print("Bad Guess!!!")
            lives-=1
    else:
        print("Letter already guessed")
        continue

#Lose condition
print("__________________________________________________")
print("GAME OVER!!!")
print("The word was",word)