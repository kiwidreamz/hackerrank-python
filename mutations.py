# Read a given string, change the character at a given index and then print the modified string.

def mutate_string(string, position, character):
    
    string = string[:position] + character + string[position+1:]
    
    return string

