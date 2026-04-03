from display import input_user
from functions import calculate_sum


def input():

    enter = input_user("Pls enter namber >> ")
    number = float(enter)

    result = calculate_sum(number)

    return result

print(input())