year = 2000
# Computer understands only 0 and 1
# Every value other than 0 computer considers it as true(1) value.
# iteration 1 => while year => while 2000 => while true => will go inside the loop.
# iteration 2 => while year => while 2001 => while true => will go inside the loop.
while year:
  # line 3 to 7 inside while loop.
  # at 2020, it will go inside IF and will find a break and then loop will be exited.
  if year == 2020:
    print('This is current year %s' % year)
    break
  print(year)
  year = year + 1 # increasing the year in every iteration.
