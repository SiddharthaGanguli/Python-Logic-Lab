# Find the second largest number 
'''
example 1: [4,5,6,7,8,2] -> 7
example 2: [6,2,3,9,9,8] -> 8
example 3: [6,6,6,6] -> None
example 4: [-5,-8,-12,-5] -> -5


'''
def find_second_largest(numbers):
    if len(numbers) < 2:
        return None

    maximum = numbers[0]
    second_maximum = None

    for number in numbers:
        # Case A: Is this a new largest number?
        if number > maximum:
            # Move the old largest into second place
            second_maximum = maximum

            # Store the new largest number
            maximum = number

        elif number < maximum:
            # Update the second place if it is empty
            # or the current number is bigger than second maximum
            if second_maximum is None or number > second_maximum:
                second_maximum = number

        # Numbers equal to maximum are ignored

    return second_maximum


print(find_second_largest([4, 5, 6, 7, 8, 2]))
print(find_second_largest([6, 2, 3, 9, 9, 8]))
print(find_second_largest([6, 6, 6, 6]))
print(find_second_largest([-5, -8, -12, -5]))