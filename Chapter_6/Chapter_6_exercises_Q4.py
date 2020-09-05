# You need to run a loop for 15 years i.e 15 times.
# You need to print weight for each year like 1st year -> weight
# Your total at end of 15 years on moon and earth
# Every year your earth weight is increasing by 1 kg.
neev_earth_weight = 63 # Initial weight on earth
total_neev_moon_weight  = 0 # total moon weight is 0 since you are still on earth
year = 1
for number in range(0, 15):
  # you have gone to moon in every iteration
  print('%s year------------------' % year) # Weight on earth in 'n year' where n = 1,2,3,.....,15
  print('Earth weight %s' % neev_earth_weight)
  neev_moon_weight = 0.165 * neev_earth_weight # Weight on moon in 'n year' where n = 1,2,3,.....,15
  print('Moon weight %s' % neev_moon_weight)
  total_neev_moon_weight = total_neev_moon_weight + neev_moon_weight # Sum of your all moon weights
  year = year + 1 # Increasing the year
  neev_earth_weight = neev_earth_weight + 1 # Increasing your earth weight by 1 as per question.
print('Moon weight at end of 15 years %s' % total_neev_moon_weight) # Total weight on moon after 15 years

