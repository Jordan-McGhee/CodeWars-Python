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

"""

Take a Number And Sum Its Digits Raised To The Consecutive Powers And ....¡Eureka!!
The number 89 is the first integer with more than one digit that fulfills the property partially introduced in the title of this kata. What's the use of saying "Eureka"? Because this sum gives the same number.

In effect: 89 = 8^1 + 9^2

The next number in having this property is 135.

See this property again: 135 = 1^1 + 3^2 + 5^3

We need a function to collect these numbers, that may receive two integers a, b that defines the range [a, b] (inclusive) and outputs a list of the sorted numbers in the range that fulfills the property described above.

Let's see some cases:

sum_dig_pow(1, 10) == [1, 2, 3, 4, 5, 6, 7, 8, 9]

sum_dig_pow(1, 100) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 89]
If there are no numbers of this kind in the range [a, b] the function should output an empty list.

sum_dig_pow(90, 100) == []

"""

def sum_dig_pow(a, b):
    
    # empty list to append working numbers to
    answer = []

    # iterate over nums in range a to b+1 since we need to include b
    for num in range(a,b+1):

        # convert each num in our range to string in order to iterate over its individual numbers
        string_num = str(num)
        # total variable set equal to 0 for each iteration
        total = 0

        # iterate over each character in our number that we converted to a string. Use enumerate to get the index. We'll use the index + 1 to raise the current character to that power.
        for i,char in enumerate(string_num):
            # +1 because our index will start at 0
            i += 1
            
            # add the integer value of our character raised to the i power
            total += (int(char) ** i)

        # check if our total variable is equal to the current number that we're on
        if total == num:
            # if so, our condition is met to add this num to our answer variable from before
            answer.append(num)

    return answer