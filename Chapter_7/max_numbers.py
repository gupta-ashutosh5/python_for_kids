import sys


def maximum(list):
    largest = list[0]
    for number in list:
        if number > largest:
            largest = number

    return largest


user_choice = 'y'
while user_choice == 'y':
    print("Provide 3 numbers.")
    list_of_numbers = [int(sys.stdin.readline()), int(sys.stdin.readline()), int(sys.stdin.readline())]
    print("This is the highest number:")
    print(maximum(list_of_numbers))

    print("Do you want to continue[y/n]?")
    user_choice = input()
    # Used input instead of readline() because readline() function reads escape character as well.
    # user_input = sys.stdin.readline() -> user_input has value 'y \n'

user_input2 = input() # only t is stored
user_input3 = sys.stdin.readline() # u \n(newline character) one more single line
print(user_input2)
print(user_input3 == 'u') #prints FALSE
print(user_input3 == 'u\n') #prints TRUE