# 1. number in ninjas < 50 => print That's too many
# 2. number in ninjas < 30 => print "It will be a struggle"
# 3. number in ninjas < 10 => print 'I can fight those ninjas'

ninjas = 49
# if ninjas >=30 and ninjas < 50 => print That's too many
# if ninjas >=10 and ninjas < 30 => print "It will be a struggle"
# if ninjas < 10 print 'I can fight those ninjas'

print('Ninjas = %s' % ninjas)

if ninjas >= 30 and ninjas < 50:
  print('That\'s too many')
elif ninjas >= 10 and ninjas < 30:
  print('It will be a struggle')
elif ninjas < 10:
  print('I can fight those ninjas')
