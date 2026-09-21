# Move Zeros

def moveZero(numbers):
    position=0
    for i in range(len(numbers)):
        if numbers[i]!=0:
            numbers[position],numbers[i]=numbers[i],numbers[position]
            position+=1
    return numbers

print(moveZero([1,2,0,3,5,0,1,4,2,0,8]))