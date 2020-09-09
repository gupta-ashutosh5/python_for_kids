neev_earth_weight = 63
total_neev_mars_weight  = 0
year = 1
for number in range(0, 25):
  print('%s year------------------' % year)
  print('Earth weight %s' % neev_earth_weight)
  neev_mars_weight = 0.5 * neev_earth_weight
  print('Mars weight %s' % neev_mars_weight)
  total_neev_mars_weight = total_neev_mars_weight + neev_mars_weight
  year = year + 1
  neev_earth_weight = neev_earth_weight + 3.
print('Mars weight at end of 25 years %s' % total_neev_mars_weight)
