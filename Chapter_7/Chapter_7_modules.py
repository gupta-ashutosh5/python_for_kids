# Lets talk about sys module.
# sys module has object stdin to take input from terminal/screen.
import sys

# Using . operator you can call functions in a modules.
print(sys.stdin.readline())

numberAsInput = int(sys.stdin.readline())
# If you are not converting it into integer, then it will be seen as string by default.
print(numberAsInput)

# Here sys -> module
# stdin -> file object
# readline -> function which takes input from terminal