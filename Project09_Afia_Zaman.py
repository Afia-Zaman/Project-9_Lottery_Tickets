
# Create constants for the number of numbers in a ticket and the max/min allowed numbers on the ticket.
NUM_OF_NUMBERS = 7
MIN_NUMBER = 1
MAX_NUMBER = 100
import random

# Determine valid input number
def in_range(number):
    return MIN_NUMBER <= number <= MAX_NUMBER

# Determine list of the number of a winning ticket
def generate_winning_ticket():
    lottery_num_list = []
    for x in range(NUM_OF_NUMBERS):
        winning_num = random.randint(MIN_NUMBER, MAX_NUMBER)
        if winning_num not in lottery_num_list:
            (lottery_num_list.append(winning_num))
    lottery_num_list.sort()
    return lottery_num_list

# Determine the ticket which will win
def won_the_lottery(player_ticket):
    winning_ticket = generate_winning_ticket()
    player_ticket.sort()
    return player_ticket == winning_ticket


def main():
    print("Let's play the lottery!")
    print()

# write a for loop that asks the user for their 7 lottery numbers, storing each number in a list
    player_ticket = []
    for x in range(NUM_OF_NUMBERS):
        number = int(input(f"Number #{x+1}: "))

# an input validation loop for the numbers entered by the user
        while not in_range(number) or number in player_ticket:
            number = int(input("Not in range or duplicate, try again: "))
        player_ticket.append(number)

# Print the winning or defeated message
    if won_the_lottery(player_ticket):
        print("\nYou won!")
    else:
        print("\nDefeated!")


main()


