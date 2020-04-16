# GUESSING NUMBER GAME

from random import randint

secret_number = randint(1, 10)
number_of_trials = set()


def guessing_game():
    while True:
        try:  # Avoiding a ValueError using the try and except block
            user_guess = int(input('guess the secret number between 1~10: '))  # checking if number is within the range
            if user_guess in range(1, 11):
                # checking if user gets the secret number
                if user_guess == secret_number:
                    print('\nCongrats!!!, You guessed the secret number')
                    break

                # Telling the user if the guessed number is either greater of lesser than the secret number
                # and also adding the user's guessed number to the empty set above

                elif user_guess != secret_number and user_guess > secret_number:
                    number_of_trials.add(user_guess)
                    print('Your guess is greater than secret number. Try again!')

                elif user_guess < secret_number and user_guess != secret_number:
                    number_of_trials.add(user_guess)
                    print('Your guess is less than the secret number. Try again!')
                    continue
            else:
                print('\nEnter a number within the range of 1~10')

        except ValueError as err:
            print(f'Error code: {err}. Enter only numbers, Thanks.')

    print(f'\nThe number_of_trials you used before guessing the secret number  is:  {len(number_of_trials)}')

# Running the function
guessing_game()

response = input('\nDo you wanna play again (y/n): ')
if response == 'y':
    guessing_game()

else:
    print('Thanks for playing')
    exit()




