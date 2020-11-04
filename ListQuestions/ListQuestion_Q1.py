# Get all inputs from user.


def count_strings_length_more_than_one(user_list):
  # Take count = 0
  count = 0
  for value in user_list:
    # Calculate length of string.
    str_length = len(value)
    if str_length >= 2:
      # Get first char and last char.
      first_char = value[0]
      last_char = value[str_length - 1]
      if first_char == last_char:
        # Increment count by 1.
        count = count + 1
  print(count)


user_list = [
  input('First String:'),
  input('Second String:'),
  input('Third String:'),
  input('Fourth String:')
]

count_strings_length_more_than_one(user_list)
