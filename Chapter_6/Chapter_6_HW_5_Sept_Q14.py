#14. Given a number n, find sum of its digits. If n = 21, sum = 2+1 = 3

#Solution:
# Generalisation  or finding a pattern
# i/o = 12, o/p = 3 = 1 + 2
# i/o = 51, o/p = 6 = 5 + 1
# In every sum problem, always have a variable sum = 0

# Steps:
# 1. Suppose you have a n = 109.
# 2. Output is 1 + 0 + 9 = 10.
# 3. Separate digits from number in reverse order like
  # 1st separate 9 from n -> add it to sum = 9  -> new n =  10
  # 2nd separate 0 from n -> add it to sum = 9 + 0 = 9 -> new n= 1
  # 3rd separate 1 from n -> add it to sum = 9 + 1 = 10 -> new n = 0 -> execution stops

  # start from n and go till 0

# Repeat these 3 steps while n > 0
# How to get the removed digit?
 # removed_digit = n%10 = 109 % 10 = 9

# Add the removed digit to sum?
  # sum = sum + removed_digit = 0 + 9 = 9

# How to separate a digit from a number?
 # n  = n//10 ; n = 109 // 10 = 10



# Assign a number
n = 109

# Initialise sum = 0
sum = 0

# Use while loop to check if n is remaining or not.
while (n > 0) :
  # Add digits to sum
  sum = sum + n%10
  # Remove digits from number
  n = n // 10

# Finally print sum ot of loop.
print(sum)

