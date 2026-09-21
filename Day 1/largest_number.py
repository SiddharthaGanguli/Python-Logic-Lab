# Write a python program to find the largest number .
'''
Example 1 : [1,2,3,5,6,8] in this case the largest number will be the 8
Example 2 : [-8,-4,-2,-12] in this case the largerst number will be the -3


# # Don't use any funtions like max(),sort(),sorted()
'''


def find_largest_number(numbers):
    max=numbers[0]

    for num in range (len(numbers)):
        if numbers[num] > max :  
            max = numbers[num]
    return max


print(find_largest_number([1,2,3,5,6,8]))



