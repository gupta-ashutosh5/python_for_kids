#8. Given a list iterate it and display numbers which are divisible by 5 and if you find number greater than 150 stop the loop iteration
# list1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]

# Solution:
# 1. You have a list/series of numbers.
# 2. Find numbers which are divisible by 5 in the list and display these numbers.
# 3. Come out of the loop when number is greater than 150.

list = [3, 10, 105, 121, 142, 145, 160]
#printed - 10, 105, 145
for number in list:
  # First we need to check if number > 150 or not.
  if number > 150:
    break
  # Second if number is divisible by 5, then display.
  if number%5 == 0:
    print(number)
