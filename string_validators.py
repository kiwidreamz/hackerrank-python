#You are given a string S. Your task is to find out if the string S contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.

if __name__ == '__main__':
    s = input()
    alnum = []
    alpha = []
    digit = []
    lower = []
    upper = []
    
    for i in range(len(s)):
        if s[i].isalnum():
            alnum.append(True)
        else:
            alnum.append(False)
        
        if s[i].isalpha():
            alpha.append(True)
        else:
            alpha.append(False)
            
        if s[i].isdigit():
            digit.append(True)
        else:
            digit.append(False)
            
        if s[i].islower():
            lower.append(True)
        else:
            lower.append(False)
        
        if s[i].isupper():
            upper.append(True)
        else:
            upper.append(False)
            
            
    for i in range(len(alnum)):
        if alnum[i] == True:
            first = True
            break
        else:
            first = False
    for i in range(len(alpha)):
        if alpha[i] == True:
            second = True
            break
        else:
            second = False
    for i in range(len(digit)):
        if digit[i] == True:
            third = True
            break
        else:
            third = False
    for i in range(len(lower)):
        if lower[i] == True:
            fourth = True
            break
        else:
            fourth = False
    for i in range(len(upper)):
        if upper[i] == True:
            fifth = True
            break
        else:
            fifth = False
            
            
    
    print(first)
    print(second)
    print(third)
    print(fourth)
    print(fifth)
    