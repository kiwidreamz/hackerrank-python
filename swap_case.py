# You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

def swap_case(s):
    
    s2 = ""
    i2 = ""
    
    for i in s:
        if i.isupper():
            i2 = i.lower()
            s2 = s2 + i2
        else:
            i2 = i.upper()
            s2 = s2 + i2

        
    
    return s2