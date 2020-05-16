# Write a function that takes a list of characters and reverses the letters in place.

def reverse_characters(chars):
  for i in range(len(chars) // 2):
    temp = chars[i]
    chars[i] = chars[-1 - i]
    chars[-1 - i] = temp
  return chars


my_chars = ['h', 'e', 'l', 'l', 'o']
print(reverse_characters(my_chars))


'''
Time: O(n)
Space: O(1)

Space complexity is constant because the characters are reversed in place.
'''