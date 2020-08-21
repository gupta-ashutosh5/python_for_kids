money = 2000
# 1. Money is greater than 100 and Money is less than 500
# OR
# 2. Money is greater than 1000 and Money is less than 5000
if (money > 100 and money < 500) or (money > 1000 and money < 5000):
  print('Money is %s' % money)
else:
  print('Money is neither between 100 and 500 nor between 1000 and 5000')

# In computers we work in binary either 1 or 0.
# OR operator means addition
# 1 = true and 0 = false
# 1 or 1 = 1   |  true or true = true
# 1 or 0 = 1   |  true or false = true
# 0 or 1 = 1   |  false or true = true
# 0 or 0 = 0   |  false or false = false

# AND operator means multiplication
# 1 AND 1 = 1 | true AND true = true
# 1 AND 0 = 0 | true AND false = false
# 0 AND 1 = 0 | false AND TRUE  = false
# 0 AND 0 = 0 | false AND FALSE = false

# money = 2000 assigning 2000 to money
# Statement: money > 100 = TRUE = 1
# AND
# Statement: money < 500 = FALSE = 0
# This becomes (money > 100 and money < 500) = 1 AND 0 = 0

# OR

# Statement: money > 1000 = TRUE = 1
# AND
# Statement: money < 5000 = TRUE = 1
# This becomes (money > 1000 and money < 5000) = 1 AND 1 = 1

# Final expression 0 OR 1 = 0 + 1 = 1
# IF(1) => IF(true) => print the statement
