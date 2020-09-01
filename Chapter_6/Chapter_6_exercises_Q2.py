# In this program, we are going to use `//` and `%` operator.
# `//` operator means perform division, but the output will come as quotient.
# Example: 15 // 2 = 7 i.e. When 15 is divided by 2, the quotient is 7. Thus the output is 7
# Example: 22 // 3 = 7 i.e. When 22 is divided by 3, the quotient is 7. Thus the output is 7

# `%` operator means perform division, but the output will come as remainder.
# Example: 15 % 2 = 1 i.e. When 15 is divided by 2, the remainder is 1. Thus the output is 1
# Example: 22 % 3 = 1 i.e. When 22 is divided by 3, the remainder is 1. Thus the output is 1
age = 14
start = 0
# Check if age is even or odd.
# Check even age
if age % 2 == 0:
  start = 2
  # In case of 14, we need to run loop 7 times i.e 14 // 2 = 7 i.e age // 2
  # In case of 16, we need to run loop 8 times i.e 16 //2 = 8 i.e. age // 2
  # Similarly, in case of 100 we need to run loop 50 times i.e. 100 // 2 = 50 i.e age // 2
  # Thus end value = age // 2.
  end = age // 2
else:
  start = 1
  # In case of 13, we need to run loop 7 times i.e 13 // 2  + 1 = 7 i.e age // 2 + 1
  # In case of 15, we need to run loop 8 times i.e 15 //2 + 1 = 8 i.e. age // 2 + 1
  # Similarly, in case of 99 we need to run loop 50 times i.e. 99 // 2  + 1 = 50 age // 2 + 1
  # Thus end value  = age // 2.
  end = age // 2 + 1

# Print numbers till age
for number in range(0, end):
  print(start)
  start = start + 2
