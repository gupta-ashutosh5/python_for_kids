# We have a list here.
ingredients = ['snails', 'leeches', 'gorilla belly-button lint', 'caterpillar eyebrows', 'centipeded toes']
# Print
# 1 snails
# 2 leeches
# 3 gorilla belly-button lint
# 4 caterpillar eyebrows
# 5 centipeded toes
ingredient_position = 1
for ingredient in ingredients:
  print('%s %s' % (ingredient_position, ingredient))
  ingredient_position = ingredient_position + 1
