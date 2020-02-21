# Answers

## Exercise I

a) O(n), In this loop you are adding the squared and looping until you reach the cubed.
This can be simplified down to just looping n times by canceling Ns out of the condition
and accumulator

b) O(n log n), You have two loops, one that is looping through every item, one that is
looping through half of the current items. The first loop is O(n) the second is O(log n)
so in total it would result in O(n log n)

c) O(n), You have a recursive function that subtracts 1 from n on each loop until it reaches 0
at which point it unravels adding two to each n accumulating the total. Since the adding of 2
doesn't result in reaching the base case any faster this is strictly linear.

## Exercise II

This is just binary search.

1. You start with the midpoint between the bottom floor and the top floor.
2. Then you drop an egg.
3. If it breaks then you go to the midpoint between the bottom floor and where you are now.
4. If it doesn't then you go to the mid point between the top floor and where you are now.
5. Repeat steps 2-5 until you have determined what is the lowest floor an egg will break.
