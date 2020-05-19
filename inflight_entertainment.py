'''
You've built an inflight entertainment system with on-demand movie streaming.

Users on longer flights like to start a second movie right when their first one ends, but they complain that the plane usually lands before they can see the ending. So you're building a feature for choosing two movies whose total runtimes will equal the exact flight length.

Write a function that takes an integer flight_length (in minutes) and a list of integers movie_lengths (in minutes) and returns a boolean indicating whether there are two numbers in movie_lengths whose sum equals flight_length.

When building your function:

  Assume your users will watch exactly two movies
  Don't make your users watch the same movie twice
  Optimize for runtime over memory
'''


'''
1st solution: brute force
  Time: O(n^2)
  Space: O(1)

We can do better, although sacrificing the space complexity.

2nd solution: use a hash table (Python dictionary)
  Time: O(n)
  Space: O(n)
'''

def can_two_movies_fill_flight(movie_lengths, flight_length):

    cache = {}

    for i, first_movie_length in enumerate(movie_lengths):
        other_movie = flight_length - first_movie_length
        if other_movie in cache:
            return True

        cache[first_movie_length] = i

    return False


list_of_movies_lengths = [1, 2, 3, 4, 5, 6]
flight_total_time = 11

print(can_two_movies_fill_flight(list_of_movies_lengths, flight_total_time))