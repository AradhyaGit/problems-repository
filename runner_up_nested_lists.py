if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
        
    grades = sorted(list(set([student[1] for student in students])))
    second_lowest_grade = grades[1]
    
    runner_ups = [student[0] for student in students if student [1] == second_lowest_grade]
    runner_ups.sort()
    
    for name in runner_ups:
        print(name)
