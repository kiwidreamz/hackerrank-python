# In this challenge, the task is to debug the existing code to successfully execute all provided test files.

def is_vowel(letter):
    return letter in ['a', 'e', 'i', 'o', 'u', 'y']

def score_words(words):
    score = 0
    word = ""
    for word in words:
        num_vowels = 0
        for letter in word:
            if is_vowel(letter):
                num_vowels += 1
        if num_vowels % 2 == 0:
            score += 2
            #print(score)
        else:
            score += 1
            #print(score)
    return score

