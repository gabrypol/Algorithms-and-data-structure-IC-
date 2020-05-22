'''
You want to build a word cloud, an infographic where the size of a word corresponds to how often it appears in the body of text.

To do this, you'll need data. Write code that takes a long string and builds its word cloud data in a dictionary, where the keys are words and the values are the number of times the words occurred.

Think about capitalized words. For example, look at these sentences:

  'After beating the eggs, Dana read the next step:'
  'Add milk and eggs, then add flour and sugar.'
What do we want to do with "After", "Dana", and "add"? In this example, your final dictionary should include one "Add" or "add" with a value of 22. Make reasonable (not necessarily perfect) decisions about cases like "After" and "Dana".

Assume the input will only contain words and standard punctuation.

You could make a reasonable argument to use regex in your solution. We won't, mainly because performance is difficult to measure and can get pretty bad.
'''

def word_cloud_data(input_string):
  words_list = []
  current_word_start_index = 0
  current_word_length = 0
  for i, char in enumerate(input_string):
    if len(input_string) - 1 != i and (char.isalpha()  or ((char == "'" or char == "-") and input_string[i - 1].isalpha() and input_string[i + 1].isalpha())):
      if current_word_length == 0:
        current_word_start_index = i
      current_word_length += 1

    elif char.isalpha() and len(input_string) - 1 == i:
      word = input_string[current_word_start_index:]
      words_list.append(word)
    else:
      word = input_string[current_word_start_index:current_word_start_index + current_word_length]
      words_list.append(word)
      current_word_length = 0

  # Now I create a list without empty strings and making sure that all characters of the string are lowercase
  my_clean_least = []
  for string in words_list:
    if string != '':
      my_clean_least.append(string.lower())

  my_dict = {}
  for string in my_clean_least:
    if string in my_dict:
      my_dict[string] += 1
    else:
      my_dict[string] = 1
  return my_dict


my_string = 'After beating the eggs, Dana read the next step'
my_string = 'Add milk and eggs, then add flour and sugar.'
my_string = 'I like cake'
my_string = 'Chocolate cake for dinner and pound cake for dessert-'
my_string = 'Strawberry short cake? Yum!'
my_string = 'Dessert - mille-feuille cake'
my_string = 'Mmm...mmm...decisions...decisions'
my_string = "Allie's Bakery: Sasha's Cakes"
print(word_cloud_data(my_string))


'''
Time: O(n)
Space: O(n)
'''