# Initially he has 20 coins.
found_coins = 20

#Every day 10 coins are being added
coins_added_every_day = 10

#Each week 3 coins are being stolen.
stolen_coins_per_week = 3

# Find total coins at end of year.
coins_added_every_week = 7 * coins_added_every_day # 70

# position of coins at week 0 or start.
total_coins_at_end_of_week = found_coins

# loop will run 52 times.
for week in range(1,53):
  total_coins_at_end_of_week = total_coins_at_end_of_week + coins_added_every_week - stolen_coins_per_week
  # 1 -> 20 + 70 - 3 = 87
  # 2 -> 87 + 67 = 154
  print('Week %s = %s' % (week, total_coins_at_end_of_week))
