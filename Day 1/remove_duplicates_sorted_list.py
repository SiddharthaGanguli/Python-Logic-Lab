# remove duplicates from a sorted list 

def remove_duplicates(numbers):
    numbers=list(numbers)
    position=1

    for num in range(len(numbers)):
        if numbers[num]==numbers[position]:
            numbers.pop(num)
            
print(remove_duplicates([1,2,1,2,2,1,5]))