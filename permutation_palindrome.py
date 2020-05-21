'''
Write an efficient function that checks whether any permutation of an input string is a palindrome.

You can assume the input string only contains lowercase letters.

Examples:

"civic" should return True
"ivicc" should return True
"civil" should return False
"livci" should return False

"But 'ivicc' isn't a palindrome!"
If you had this thought, read the question again carefully. We're asking if any permutation of the string is a palindrome. Spend some extra time ensuring you fully understand the question before starting. Jumping in with a flawed understanding of the problem doesn't look good in an interview.
'''

'''
A brute force approach would be very expensive (n!n) in term of runtime.
I can do better than that using a hash map (Python dictionary) and store the occurrences of each char in the input string. If more than one char has an odd occurrence, then no permutation of the input string is a palindrome. Using this approach, the time complexity will be linear and the space complexity constant (read below after the solution).
'''

def has_palindrome_permutation(the_string):
  my_dict = {}

  for char in the_string:
    if char in my_dict:
      my_dict[char] += 1
    else:
      my_dict[char] = 1
  print(my_dict)

  chars_with_odd_occurrences = 0
  for char in my_dict:
    if my_dict[char] % 2 != 0:
      chars_with_odd_occurrences += 1

  if chars_with_odd_occurrences > 1:
    return False
  else:
    return True


my_string = "aabbc" #returns True because only one letter ("k") has an odd number of occurrences.
my_string = "aabbcd" #returns False because more than one char ("c" and "d") have an odd number of occurrences.
print(has_palindrome_permutation(my_string))

'''
Time: O(n)
Space: O(1) where k is the number of available characters in ASCII or Unicode. ASCII has 128 different characters, while Unicode 110'000. Both numbers can be approximated to a constant.
'''