from random import randint


red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]

green = 0

black = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]


def is_red(num: int) -> bool:
    #Check if given number is red.
    if num in red:
        return True
    else:
        return False


def is_black(num: int) -> bool:
    #Check if given number is black.
    if num in black:
        return True
    else:
        return False


def is_green(num: int) -> bool:
    #Check if given number is green
    if num == 0:
        return True
    else:
        return False


def is_even(num: int) -> bool:
    #Check if given number is even.
    if num % 2 == 0:
        return True
    else:
        return False


def is_odd(num: int) -> bool:
    #Check if given number is odd.
    if is_even(num):
        return False
    else:
        return True


def in_first_half(num: int) -> bool:
    #Check if given number in first half.
    if 0 < num <= 18:
        return True
    else:
        return False


def in_second_half(num: int) -> bool:
    #Check if given number in second half.
    if in_first_half(num) or is_green(num):
        return False
    else:
        return True


def in_which_third(num: int) -> int:
    #Find in which third the given number.
    if 0 < num < 13:
        return 1
    elif 13 < num < 25:
        return 2
    elif 25 < num < 37:
        return 3
    else:
        return 0


def is_right_third(given_third: int, right_third: int) -> bool:
    #Check if given number == right third.
    if in_which_third(right_third) == given_third:
        True
    else:
        False 


def in_which_line(num: int) -> int:
    #Find in which line the given number.
    if num % 3 == 0 and not is_green(num):
        return 1
    elif num % 3 == 1:
        return 3
    elif num % 3 == 2:
        return 2
    else:
        return 0


def is_right_line(given_line: int, right_line: int) -> bool:
    #Check is given number == right line.
    if in_which_line(right_line) == given_line:
        return True
    else:
        return False


def check_bet_add_ballance(bet: int, ballance: int, multiply: int, checking: bool) -> int:
    #Check if bet win and change balance.
    if checking:
        bet *= multiply
        print(f"Your bet has won\n\
+{bet}")
    else:
        bet = 0
        print("Your bet is lost")
    ballance += bet
    return ballance


ballance = 1000


while ballance > 0:
    bet_amount = abs(int(input(f"You have {ballance}$ \nHow much you want to bet: ")))



    print(f"Your bet: {bet_amount}$")
    if bet_amount <= ballance:
        ballance -= bet_amount
        print("List of position: \n\
            1. Numbers (from 0 to 36) \n\
            2. Even or Odd\n\
            3. Which line (From Line 1 to Line 3 \n\
            4. Which third (From Third 1 to Third 3 \n\
            5. Which colour (Red or Black) \n\
            6. Which half(Half 1 or Half 2)")

        ruletka = randint(0, 36)

        bet_pos = input(f"In which position you want to bet: ")

        if bet_pos.isnumeric():
            ballance = check_bet_add_ballance(bet_amount, ballance, 36, ruletka == int(bet_pos))
            if not is_green(ruletka):
                print(f"Roulette: {ruletka}")

        if not is_green(ruletka):
            if bet_pos.lower() == "even":
                ballance = check_bet_add_ballance(bet_amount, ballance, 2, is_even(ruletka))
                if is_even(ruletka):
                    print(f"Roulette: {ruletka} Even")
                else:
                    print(f"Roulette: {ruletka} Odd")

            if bet_pos.lower() == "odd":
                ballance = check_bet_add_ballance(bet_amount, ballance, 2, is_odd(ruletka))
                if is_odd(ruletka):
                    print(f"Roulette: {ruletka} Odd")
                else:
                    print(f"Roulette: {ruletka} Even")

            if bet_pos[0:4].lower() == "line":
                ballance = check_bet_add_ballance(bet_amount, ballance, 3, is_right_line(int(bet_pos[-1]), ruletka))
                if in_which_line(ruletka) == 1:
                    print(f"Roulette: {ruletka} First line")
                elif in_which_line(ruletka) == 2:
                    print(f"Roulette: {ruletka} Second line")
                else:
                    print(f"Roulette: {ruletka} Third line")

            if bet_pos[0:5].lower() == "third":
                ballance = check_bet_add_ballance(bet_amount, ballance, 3, is_right_third(int(bet_pos[-1]), ruletka))
                if in_which_third(ruletka) == 1:
                    print(f"Roulette: {ruletka} First third")
                elif in_which_third(ruletka) == 2:
                    print(f"Roulette: {ruletka} Second third")
                else:
                    print(f"Roulette: {ruletka} Third third")

            if bet_pos.lower() == "red":
                ballance = check_bet_add_ballance(bet_amount, ballance, 2, is_red(ruletka))
                if is_red(ruletka):
                    print(f"Roulette: {ruletka} Red")
                else:
                    print(f"Roulette: {ruletka} Black")

            if bet_pos.lower() == "black":
                ballance = check_bet_add_ballance(bet_amount, ballance, 2, is_black(ruletka))
                if is_red(ruletka):
                    print(f"Roulette: {ruletka} Red")
                else:
                    print(f"Roulette: {ruletka} Black")

            if bet_pos[0:4].lower() == "half":
                if int(bet_pos[-1]) == 1:
                    ballance = check_bet_add_ballance(bet_amount, ballance, 2, in_first_half(ruletka))
                elif int(bet_pos[-1]) == 2:
                    ballance = check_bet_add_ballance(bet_amount, ballance, 2, in_second_half(ruletka))
                if in_first_half(ruletka):
                    print(f"Roulette: {ruletka} First half")
                else:
                    print(f"Roulette: {ruletka} Second half")
        else:
            print(f"Roulette {ruletka} Its green!")
    else:
        print("The bet is not correct, try again.")
