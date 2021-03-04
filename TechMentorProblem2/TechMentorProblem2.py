# Write a function that accepts a non-empty array of distinct integers and an integer representing a target value.
# If any two numbers in the input array sum up to the target value, the function should return those two numbers in any order.
# If no two numbers in the input array sum up to the target value, the function should return an empty array.
# There will be at most one pair of numbers in any input array summing up to the target value.


# Understand problem:

# args: array, target value
# return two numbers within array that add up to target val
# return empty array if nothing adds up to TV
# Givens: only one correct pair, if no correct pair return empty array, integers


# Ex in/out:

# in: [1,2,3,4], 8      out: []
# in: [1,2,3,4], 7      out: [3, 4]
# in: [1,2,4,5], 7      out: [2, 5]
# in: [3,4,2], 7        out: [3, 4]
# in: [1], 1            out: []


# Questions:

# Questions: output type: array
# Questions: cannot return one number that equals TV, must return two or none
# Questions: Can there be one item in array? Yes, must return empty array


# Brute Force/ PseudoCode:

# for every item in the input array, add every other number indiviually and compare it to the target value. if they are equal,
# return the pair in an array.
# after comparing every combination, if none are equal to the target, return []


# Optimize/Pseudocode or Other COA: for every int in input array, if any number AFTER(use [index:]) it, added to the int, equals TV then return arr of those two
# Needs to verify that the returned numbers aren't the same int, can easily check with /2 since numbers are distinct prior to returning
# Returns [] if it checks every number in input arr and doesn't find a match


# Actual code:

def findSum(li, target):
    counter = 0
    for num in li:
        if (target - num in li[counter:] and target / 2 != num):
            return [num, target - num]
        counter += 1
    return []

# Tests:

print(findSum([1,2,3,4], 8))
print(findSum([1,2,3,4], 7))
print(findSum([1,2,4,5], 7))
print(findSum([3,4,2], 7))
print(findSum([1], 1))
