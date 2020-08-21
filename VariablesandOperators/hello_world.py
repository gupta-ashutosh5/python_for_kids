test = '''Hello neev.
How are you?''
print(test)'''

print(test)

silly_string = 'He said, Aren\'t'
three_quotes_string = '''He said, Aren't'''
print(silly_string)
print(three_quotes_string)

myscore = 1000
message = 'I scored %s points'
print(message) # ouput comes as a string. %s is considered a string.
# the %s - variable holder - is being replaced by variable value.
print(message % myscore) #in output %s is being replaced by variable value
# the %s is not being replaced

golf_score = 84
# Problem - print (Best score of Neev is 84 points.)
message = 'Best score of Neev is %s points.'
print(message % golf_score)

# Usage without variable.
name = 'Neev'
print('My name is %s' % name)

print(" --------Can replace same placeholder by different values.-----------")
message = 'My name is %s'
ashutosh = 'Ashutosh'
neev = 'Neev'
print(message % ashutosh)
print(message % neev)

print('-------------Two placeholders in a single statement--------------------')
message = '%s is teaching computers to %s'
print(message % (ashutosh, neev))

print(10 * "Hello\n")

print('-----------List example-------------------')
# length of list = 5
# index range from 0 to 4 (length - 1)
shopping_list = ['Milk', 'Rice', 'Flour', 'Bread', 'Butter', 'Noodles']
print(shopping_list)
shopping_list.append('Banana') # this can be a user input.
print(shopping_list)

print('Buy %s' % str (shopping_list))
# 1 is included 3 is not included
print(shopping_list[1:3])
print('Buy 1 item %s' % (shopping_list[0]))
print('Buy 1 item %s' % (shopping_list[1]))

# Benefit of using list than string.
# string example
neev_list_to_mom = 'Buy me supreme hoodie, adidas shoes'
neev_tells_friend = 'I am getting adidas shoes'
print(neev_list_to_mom)
print(neev_tells_friend)

#list example
shopping_list_neev = ['supreme hoodie', 'adidas shoes']
neev_list_to_mom = 'Buy me %s, %s'
neev_tells_friend = 'I am getting %s'
print(neev_list_to_mom % (shopping_list_neev[0], shopping_list_neev[1]))
print(neev_tells_friend % (shopping_list_neev[1]))

# which is more efficient - String/List

# delete example
deleted_item = shopping_list_neev[0] #storing 1st value in another variable.
del shopping_list_neev[0] #deleting 1st value.
print(shopping_list_neev)
shopping_list_neev.append(deleted_item) #adding again
print(shopping_list_neev)

#add 2 lists.
print(shopping_list_neev + shopping_list)

#multiply number in list
# representing a loop
print(shopping_list * 5)

#add number in list
# addtion is string + string
# operands should be of same type while doing addition.
print(shopping_list_neev[0] + "5")

#multiply 2 lists.
# error code
# print(shopping_list * shopping_list_neev)

# python map example
favorite_sports = {
  'Ralph Williams' : 'Football',
  'Michael Tippett' : 'Basketball',
  'Edward Elgar' : 'Baseball',
  'Rebecca Clarke' : 'Netball',
  'Ethel Smyth' : 'Badminton',
  'Frank Bridge' : 'Rugby'
}

print(favorite_sports['Ralph Williams'])

#In case of list favorite_sports[0]