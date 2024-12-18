import random

def get_numbers_ticket(min: int, max: int, quantity: int) -> int:
    # Check the validity of the input parameters
    if not (1 <= min <= max <= 1000 and quantity <= (max - min + 1)):
        return []

    # Generate a random list of numbers
    random_numbers = random.sample(range(min, max + 1), quantity)
    # Sort the list
    random_numbers.sort()

    return random_numbers

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Лотерейні числа:", lottery_numbers)
