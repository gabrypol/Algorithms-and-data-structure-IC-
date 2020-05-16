'''
You're working on a secret team solving coded transmissions.

Your team is scrambling to decipher a recent message, worried it's a plot to break into a major European National Cake Vault. The message has been mostly deciphered, but all the words are backward! Your colleagues have handed off the last step to you.

Write a function reverse_words() that takes a message as a list of characters and reverses the order of the words in place. ↴

Why a list of characters instead of a string?

The goal of this question is to practice manipulating strings in place. Since we're modifying the message, we need a mutable ↴ type like a list, instead of Python 3.6's immutable strings.

For example:

  message = [ 'c', 'a', 'k', 'e', ' ',
            'p', 'o', 'u', 'n', 'd', ' ',
            's', 't', 'e', 'a', 'l' ]

reverse_words(message)

# Prints: 'steal pound cake'
print(''.join(message))

When writing your function, assume the message contains only letters and spaces, and all words are separated by one space.
'''


def reverse_words(message):
  reverse_chars(message, 0, len(message) - 1)

  current_word_1st_index = 0
  for i, char in enumerate(message):
      if char == ' ':
          reverse_chars(message, current_word_1st_index, i - 1)
          current_word_1st_index = i + 1
      elif i == len(message) - 1:
          reverse_chars(message, current_word_1st_index, i)
  return message


def reverse_chars(message, left_index, right_index):
    while (left_index < right_index):
        temp = message[left_index]
        message[left_index] = message[right_index]
        message[right_index] = temp
        left_index += 1
        right_index -= 1

    return message


myMessage = ['c', 'a', 'k', 'e', ' ',
             'p', 'o', 'u', 'n', 'd', ' ',
             's', 't', 'e', 'a', 'l']
print(reverse_words(myMessage))


'''
Time: O(n)
Space: O(1)
'''