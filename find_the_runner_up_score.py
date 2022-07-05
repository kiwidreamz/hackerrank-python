# Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. Store them in a list and find the score of the runner-up.

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    
    array = list(arr)
    array.sort()
    
    i = 1
    again = True
    
    while again:
        if array[-i] == array[-(i+1)]:
            again = True
            i = i + 1
        else:
            print(array[-(i+1)])
            again = False