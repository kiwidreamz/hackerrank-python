# Enter your code here. Read input from STDIN. Print output to STDOUT

while True:
    try:
        input_text = input()
    except:
        break
    
    # Split
    if input_text[0] == "S":
        
        # Remove first four characters for every string (+ remove parentheses if it is a method)
        if input_text[2] == "M":
            word_string = input_text[4:-2]
        else:
            word_string = input_text[4:]
            
        # Loop through the word, if capital letter found then make it small and add a space before it
        length_of_word = len(word_string)
            
        for i in range(length_of_word):
            
            if ord(word_string[i]) < 97:
                        
                new_letter = chr((ord(word_string[i])) + 32)
                        
                if i>0:
                    word_string = word_string[:i] + " " + new_letter + word_string[i+1:]
                else:
                    word_string = new_letter + word_string[i+1:]
                    
        print(str(word_string))
                
    # Combine
    else:
        # if Method, find spaces, remove them, capitalize next letter and add parentheses to the end
        if input_text[2] == "M":
            word_string = input_text[4:]
            length_of_word = len(word_string)
            
            for i in range(length_of_word):

                try:
                    if ord(word_string[i]) == 32:
                        new_letter = chr((ord(word_string[i+1])) - 32)
                        word_string = word_string[:i] + new_letter + word_string[i+2:]
                        
                except:
                    # Error checking if last character is blank
                    if word_string[-1].isalnum():
                        print(str(word_string) + "()")
                    else:
                        print(str(word_string[:-1]) + "()")
                    break
                        
        # if Class, capitalize first letter, find spaces, remove them, capitalize next letter
        elif input_text[2] == "C":
            #Capitalize first letter
            word_string = input_text[4:]
            
            new_first_letter = chr((ord(word_string[0])) - 32)
            word_string = new_first_letter + word_string[1:]
            
            length_of_word = len(word_string)
            no_spaces = 0
            
            for i in range(length_of_word):

                try:
                    if ord(word_string[i]) == 32:
                        new_letter = chr((ord(word_string[i+1])) - 32)
                        word_string = word_string[:i] + new_letter + word_string[i+2:]
                        no_spaces += 1
                        
                except:
                    print(str(word_string))
                    break
                
            # If there are no spaces in the word, print the capitalized word
            if no_spaces == 0:
                print(str(word_string))
            
        # if Variable, find spaces, remove them, capitalize next letter
        else:
            word_string = input_text[4:]
            length_of_word = len(word_string)
            
            for i in range(length_of_word):

                try:
                    if ord(word_string[i]) == 32:
                        new_letter = chr((ord(word_string[i+1])) - 32)
                        word_string = word_string[:i] + new_letter + word_string[i+2:]
                        
                except:
                    print(str(word_string))
                    break
            
    
