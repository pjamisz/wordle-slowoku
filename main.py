import random
from termcolor import colored, cprint
import getpass

print_black_on_green = lambda x: cprint(x, "black", "on_green", force_color="True")
print_black_on_yellow = lambda x: cprint(x, "black", "on_yellow", force_color="True")
print_black_on_red = lambda x: cprint(x, "black", "on_red", force_color="True")


#main function giving the player feedback about his guesses
def check_guess(guess,answer):
    checked_guess = [" "," "," "," "," "]
    guess = guess.upper()
    answer = answer.upper()

    if len(guess) != len(answer):
        print_black_on_red("Wrong length of guess")
        return

    #get rid of green letters after finding them, so they are not checked anymore for yellow or white fields
    for i, letter in enumerate(guess):
        if letter == answer[i]:
            checked_guess[i] = colored(letter,"black", "on_green", force_color='True')
            answer = answer.replace(letter, '$', 1)

    #get rid of yellow letters after finding the, so they are not checked again for yellow or later white
    for i, letter in enumerate(guess):
        if letter in answer:
            checked_guess[i] = (colored(letter,"black", "on_yellow", force_color='True'))
            answer = answer.replace(letter, '$', 1)

    #if the letter is not in word, paint it white
        else:
            if checked_guess[i] == " ":
                checked_guess[i] = (colored(letter,"black", "on_white", force_color='True'))

    return checked_guess


def game_loop():


    cprint("                                Słowoku!", "red", attrs=["bold"], force_color="True")
    print(" Słowoku - gra słowna Wordle po polsku. Zgadnij polskie słowo o długości pięciu liter,\n"
          , "wpisując swoje słowa. Masz 5 szans na zgadnięcie. Jeśli litera w zgadywanym słowie jest\n",
          "na dobrej pozycji, będzie podświetlona na zielono. Jeśli jest w tym słowie, ale na innej pozycji,\n",
          "będzie podświetlona na żółto. Jeśli danej litery nie ma w zgadywanym słowie, będzie podświetlona na biało.\n")

    end_game = False
    while(end_game is not True):

        #two game types: 1. trying to guess a random word from dictionary
        #                2. another person picks a word for the player to guess (still needs to be a real word)
        print(" Wybierz tryb gry: ")
        print(" Wciśnij 1 - wybór hasła przez innego gracza.")
        print(" Inny przycisk - losowe hasło")
        game_type = input(" Wybrany tryb gry: ")

        if game_type == "1":
            answer = getpass.getpass('Podaj hasło dla gracza : ').lower()
            while len(answer) != 5 or (not answer.isalpha()) or answer not in words:
               answer = getpass.getpass("Hasło musi być polskim słowem i mieć 5 liter. Podaj hasło dla gracza: ").lower()
               print_black_on_green("Hasło zapisane poprawnie")
        else:
            answer = random.choice(words)
            print_black_on_green("Hasło zostało wylosowane")

        #set up, clear guesses

        guesses = []
        guesses_left = 5


        # player guesses until finding the answer or
        while(guesses_left > 0):

            #get a guess from the player
            guess = get_guess()
            checked_guess = check_guess(guess,answer)
            for letter in checked_guess:
                print(letter, end = " ")


            #store guess history for printing the result
            guesses.append(checked_guess)

            # check if player has found the answer
            if guess == answer:
                print()
                print("-------------------")
                for word in guesses:
                    for letter in word:
                        print(letter, end=" ")
                    print()
                print("Gratulacje!")
                print("Hasło to: " + answer)
                print("-------------------")
                break

            guesses_left -= 1
            #continue guessing if the game is not lost or won

        if guesses_left == 0:
            print()
            print("-------------------")
            for word in guesses:
                for letter in word:
                    print(letter, end=" ")
                print()
            print("Tym razem się nie udało!")
            print("Hasło to: " + answer)
            print("-------------------")

        # get decision to play again
        print("Czy chcesz zagrać ponownie?")
        decision = input("Jeśli tak, wciśnij 1: ")
        if decision != "1":
            end_game = True



def get_guess():
    guess = input("Podaj słowo u długości pięciu liter: ")
    guess = guess.lower()
    #check if the word exists in the dictionary and is of desired length
    while len(guess) != 5 or (not guess.isalpha()) or guess not in words:
        guess = input("Podaj słowo u długości pięciu liter: ").lower()

    return guess

with open("words_five_letters.txt", 'r', encoding= 'utf8') as my_file:
    words = list(my_file.read().split())

game_loop()