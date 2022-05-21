# Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

if __name__ == '__main__':
    
    input_list = [] 
    second_lowest_names = []
    scores = set()
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        input_list.append([name, score])
        scores.add(score)
        
    second_lowest_score = sorted(scores)[1]
    #print(second_lowest_score)
    
    for name, score in input_list:
        if score == second_lowest_score:
            second_lowest_names.append(name)

    sorted_result = sorted(second_lowest_names)
    
    for i in sorted_result:
        print(i)