#1: Basic Moon Weight function
#In Chapter 6, one programming puzzle was to create a for loop to determine your weight on the moon over a period of 15 years.
# That for loop could easily be turned into a function.
# Try creating a function that takes a starting weight and increases the weight amount each year.
# You might call the new function using code like this: moon_weight(30, 0.25).

#defining function
def moon_weight(start_weight, weight_increment):
  total_neev_moon_weight  = 0 # total moon weight is 0 since you are still on earth
  year = 1
  for number in range(0, 15):
    # you have gone to moon in every iteration
    print('%s year------------------' % year) # Weight on earth in 'n year' where n = 1,2,3,.....,15
    print('Earth weight %s' % start_weight)
    neev_moon_weight = 0.165 * start_weight # Weight on moon in 'n year' where n = 1,2,3,.....,15
    print('Moon weight %s' % neev_moon_weight)
    total_neev_moon_weight = total_neev_moon_weight + neev_moon_weight # Sum of your all moon weights
    year = year + 1 # Increasing the year
    start_weight = start_weight + weight_increment # Increasing your earth weight using function param as per question.


moon_weight(30, 0.25)
# moon_weight for 5 years - same code
# moon_weight for 15 years - same code
# moon-weight for 20 years - same code
# moon_weight for 100 years - same code
