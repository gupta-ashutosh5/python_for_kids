neev_bank_savings = 300
total_neev_bank_savings  = 0
year = 1
for number in range(0, 30):
  print('%s dollars------------------' % neev_bank_savings)
  print('Previous bank Savings %s' % neev_bank_savings)
  neev_bank_savings = (0.03*300) + neev_bank_savings
  print('Bank savings%s' % neev_bank_savings)
  total_neev_bank_savings = total_neev_bank_savings + neev_bank_savings
  year = year + 1 # Increasing the year
  neev_bank_savings = neev_bank_savings + 0.03*300
print('Bank Savings at end of 30 years %s' % total_neev_bank_savings)