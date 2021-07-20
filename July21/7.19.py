# COUNT THE SMILEY FACES!

"""

Given an array (arr) as an argument complete the function countSmileys that should return the total number of smiling faces.

Rules for a smiling face:

Each smiley face must contain a valid pair of eyes. Eyes can be marked as : or ;
A smiley face can have a nose but it does not have to. Valid characters for a nose are - or ~
Every smiling face must have a smiling mouth that should be marked with either ) or D
No additional characters are allowed except for those mentioned.

Valid smiley face examples: :) :D ;-D :~)
Invalid smiley faces: ;( :> :} :]


"""

def count_smileys(arr):
    # hard code all possible smiley variations
    valid_smileys = [':)', ":-)", ":~)", ":D", ":-D", ":~D", ':)', ";-)", ";~)", ";D", ";-D", ";~D"]
    
    # count variable to return after iterating over arr
    count = 0

    # iterate over arr
    for smile in arr:
        # check if the smile is in our hard-coded list
        if smile in valid_smileys:
            # if so, increment count
            count += 1

    return count

# print(count_smileys([':D',':~)',';~D',':)']))

""" OVER THE ROAD 

Task
You've just moved into a perfectly straight street with exactly n identical houses on either side of the road. Naturally, you would like to find out the house number of the people on the other side of the street. The street looks something like this:

Street
1|   |6
3|   |4
5|   |2
Evens increase on the right; odds decrease on the left. House numbers start at 1 and increase without gaps. When n = 3, 1 is opposite 6, 3 opposite 4, and 5 opposite 2.

Example
Given your house number address and length of street n, give the house number on the opposite side of the street.

over_the_road(address, n)
over_the_road(1, 3) = 6
over_the_road(3, 3) = 4
over_the_road(2, 3) = 5
over_the_road(3, 5) = 8

"""

def over_the_road(address, n):
    # Since there are an identical number of houses on both sides of the road, we can multiply n by 2 to get what would be the number of the first house on the opposite side of the road. Now, to figure out the number of the house across from the given address, we need to subtract the given address and subtract 1 as well. I'm honestly a little confused on why this works, so hopefully nobody sees this note. Solved it in one line though
    return n*2-(address-1)

"""

SUM OF MINIMUMS

Given a 2D list of size m * n. Your task is to find the sum of minimum value in each row.

For Example:

[
    [1, 2, 3, 4, 5],       # minimum value of row is 1
    [5, 6, 7, 8, 9],       # minimum value of row is 5
    [20, 21, 34, 56, 100]  # minimum value of row is 20
]
So, the function should return 26 because sum of minimums is as 1 + 5 + 20 = 26

Note: You will be always given non-empty list containing Positive values.

"""

def sum_of_minimums(numbers):
    # create empty list to store minimum values for each list in numbers
    mins = []

    # iterate over every list in numbers
    for lst in numbers:
        # append the minimum from each list to our variable list mins
        mins.append(min(lst))
    
    # return the sume of the values in mins
    return sum(mins)

# print(sum_of_minimums([ [ 7,9,8,6,2 ], [6,3,5,4,3], [5,8,7,4,5] ])) # should be 9
# print(sum_of_minimums([ [11,12,14,54], [67,89,90,56], [7,9,4,3], [9,8,6,7]])) # should be 76