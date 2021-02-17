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
        try:
            result = int(input('Please provide your number: '))
            break
        except ValueError:
            print('Provided value is not a number, please try again!')
    return result


def guessing_the_number():
    user_number = user_choice()
    comp_number = computer_choice()
    while user_number != comp_number:
        if user_number > comp_number:
            print('Too big!')
        elif user_number < comp_number:
            print('Too small!')
        else:
            print('Great, you have won!')


guessing_the_number()
