# Functions in python.
# Functions is a small program which takes input, processes it and gives output.
# Advantage -> you can reuse few lines / same lines of code with different values.

def total(num):
  total = 0
  for index in range(1, num + 1):
    total = total + index
  return total

print(total(2))
print(total(3))
print(total(4))
