highest_golf_score = 92
start = 0
if highest_golf_score % 2 == 0:
  start = 2
  end = highest_golf_score // 2
else:
  start = 1
  end = highest_golf_score // 2 + 1
for number in range(0, end):
  print(start)
  start = start + 2
