# this example is with single statement
age = 13
if age > 10:
  print('You age is %s' % age)

# example witb multiple statements
age = 20
if age > 18:
  # Block 1 starts here
  print('Your age is greater than 18')
  print('You are an adult')
  print('You can vote')
  if age > 15:
    # Block 2 starts here
    print('Your age is 20')
    # Block 2 ends here
  #Block 1 ends here

# example with operators == and >=
age = 19
if age >= 18:
  # Block 1 starts here
  print('Your age is greater than 18')
  print('You are an adult')
  print('You can vote')
  if age != 20:
    # Block 2 starts here
    print('Your age is %s' % age)
    # Block 2 ends here
  if age == 19:
    # Block 2 starts here
    print('Your age is %s' % age)
    # Block 2 ends here
  #Block 1 ends here

money = 2000
if money > 1000:
  print("I'm rich!!")
else:
  print("I'm not rich!!")
  print("But I might be later...")
