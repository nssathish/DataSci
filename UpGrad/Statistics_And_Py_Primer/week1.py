[  # # region Problem 1
    # # Take input using input()
    #
    # # input() takes input in form of the string
    # in_string = input()
    #
    # # here extract the two numbers from the string
    # x, y = [int(i.strip()) for i in in_string.split(",")]
    #
    #
    # # print x and y before swapping
    # print(f"x before swapping: {x}")
    # print(f"y before swapping: {y}\n")
    #
    #
    # # Writing your swapping code here
    # x, y = y, x
    #
    #
    # # print x and y after swapping
    # print(f"x after swapping: {x}")
    # print(f"y after swapping: {y}\n")
    # # endregion
]
# # region Problem 3
# k = int(input())
#
#
# def is_beautiful(k):
#     result = (k - 1) % 3
#     return True if result == 0 else False
#
#
# def is_pretty(k):
#     result = (k - 2) % 3
#     return True if result == 0 else False
#
#
# def is_sexy(k):
#     return True if k % 3 == 0 else False
#
#
# # check if the number is beautiful, pretty or sexy
# if is_beautiful(k):
#     print("beautiful")
# elif is_pretty(k):
#     print("pretty")
# elif is_sexy(k):
#     print("sexy")
#
#
# # endregion

# region Problem 4
import ast

input_list = ast.literal_eval(input())
day = input_list[0]
is_on_vacation = input_list[1]


def is_weekday(day: int) -> bool:
    return day in [1, 2, 3, 4, 5]


if is_on_vacation:
    print("10:00") if is_weekday(day) else print("off")
else:
    print("7:00") if is_weekday(day) else print("10:00")

# endregion
