# Ms. Gabriel Williams is a botany professor at District College. One day, she asked her student Mickey to compute the average of all the plants with distinct heights in her greenhouse. Complete the average function.

def average(array):
    # defining variables for later use
    our_set = set()
    sum = 0
    
    # creating a set (which will remove duplicates)
    for i in range(n):
        our_set.add(arr[i])
    
    # getting the sum of each element in the set
    for j in our_set:
        sum = sum + j
        
    # calculating the average
    result = sum / (int(len(our_set)))
    
    return result

