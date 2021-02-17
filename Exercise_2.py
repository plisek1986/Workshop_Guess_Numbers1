from random import randint


def computer_choice():
    """
    Returns: Computer number in int
    """
    # computer choice as a random number from the range 1-100
    comp_nb = randint(1, 100)
    return comp_nb


def user_choice():
    while True:
        user_number = input('Please provide your number: ')
        computer_number = computer_choice()
        try:
            user_number = int(user_number)
        except ValueError:
            print('Provided value is not a number, please try again!')
        if user_number > computer_number:
            print('Too big!')
            continue
        elif user_number < computer_number:
            print('Too small!')
            continue
        else:
            print('You win!')
        break


user_choice()
