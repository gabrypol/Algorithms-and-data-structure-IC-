'''
I want to learn some big words so people think I'm smart.

I opened up a dictionary to a page in the middle and started flipping through, looking for words I didn't know. I put each word I didn't know at increasing indices in a huge list I created in memory. When I reached the end of the dictionary, I started from the beginning and did the same thing until I reached the page I started at.

Now I have a list of words that are mostly alphabetical, except they start somewhere in the middle of the alphabet, reach the end, and then start from the beginning of the alphabet. In other words, this is an alphabetically ordered list that has been "rotated." For example:

  words = [
    'ptolemaic',
    'retrograde',
    'supplant',
    'undulate',
    'xenoepist',
    'asymptote',  # <-- rotates here!
    'babka',
    'banoffee',
    'engender',
    'karpatka',
    'othellolagkage',
  ]

Write a function for finding the index of the "rotation point," which is where I started working from the beginning of the dictionary. This list is huge (there are lots of words I don't know) so we want to be efficient here.
'''

def find_rotation_point(words):

  sorted_list = sorted(words)
  if sorted_list == words:
    return 0

  idx_floor = 0
  idx_ceiling = len(words) - 1
  first_word = words[0]
  while idx_floor < idx_ceiling:
    idx_guess = idx_floor + (idx_ceiling - idx_floor) // 2
    if words[idx_guess] > first_word:
      idx_floor = idx_guess
    elif words[idx_guess] < first_word:
      idx_ceiling = idx_guess

    if idx_floor + 1 == idx_ceiling:
      return idx_ceiling


my_words = [
  'ptolemaic',
  'retrograde',
  'supplant',
  'undulate',
  'xenoepist',
  'asymptote',
  'babka',
]
print(find_rotation_point(my_words))

'''
Time: O(logn) because I have used binary search.
Space: O(n). The space complexity would be O(1) if it wasn't for the check we are doing at the beginning: in order to check whether the input list is already sorted, I need to allocate a new list sorted_list of size n, where n is the length of the given list.
'''