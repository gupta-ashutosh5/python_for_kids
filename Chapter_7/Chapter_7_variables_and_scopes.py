#Example to show variables and scope
def variable_test():
  first_variable = 10   #scope of variable_test
  second_variable = 20  #scope of variable_test
  print(first_variable) #scope of variable_test #g. print 10

# Here this variable is out of scope of variable_test so printing this will throw error
#print(second_variable)

variable_test() # a. 1st print 10

third_variable = 30 # b. third_variable is assigned 30
def variable_test_outside_scope():
  third_variable = 40 # d. third_variable (it is local to variable_test_outside_scope fn only)is assigned 40
  print(third_variable) # e. print 40
  variable_test() # f. call variable_test

variable_test_outside_scope() #c. we are calling this function.
print(third_variable) # h. print third_variable (outside) = 30

#Output -> 10 40 10 30


