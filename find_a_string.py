# In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.

def count_substring(string, sub_string):
    
    num = 0
    
    for i in range(len(string)):
        searching = string[i:(i+len(sub_string))]
        if searching == sub_string:
            num += 1
    
    return num

