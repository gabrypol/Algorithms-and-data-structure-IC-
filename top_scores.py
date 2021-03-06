'''
You created a game that is more popular than Angry Birds.

Each round, players receive a score between 0 and 100, which you use to rank them from highest to lowest. So far you're using an algorithm that sorts in O(nlgn) time, but players are complaining that their rankings aren't updated fast enough. You need a faster sorting algorithm.

Write a function that takes:

a list of unsorted_scores
the highest_possible_score in the game
and returns a sorted list of scores in less than O(nlgn) time.

For example:

  unsorted_scores = [37, 89, 41, 65, 91, 53]
  HIGHEST_POSSIBLE_SCORE = 100

# Returns [91, 89, 65, 53, 41, 37]
sort_scores(unsorted_scores, HIGHEST_POSSIBLE_SCORE)

We’re defining nn as the number of unsorted_scores because we’re expecting the number of players to keep climbing.

And, we'll treat highest_possible_score as a constant instead of factoring it into our big O time and space costs because the highest possible score isn’t going to change. Even if we do redesign the game a little, the scores will stay around the same order of magnitude.
'''


def sort_scores(unsorted_scores, highest_possible_score):

    # Sort the scores in O(n) time
    sorted_list = []
    for i in range(highest_possible_score, -1, -1):
        for score in unsorted_scores:
            if score == i:
                sorted_list.append(score)

    return sorted_list


unsorted_scores = [37, 89, 41, 65, 91, 53]
HIGHEST_POSSIBLE_SCORE = 100
print(sort_scores(unsorted_scores, HIGHEST_POSSIBLE_SCORE))

'''
Time: O(n) Time complexity is linear because the problem assumes that the highest_possible_score is a constant (read the text above).
Space: O(n)
'''
