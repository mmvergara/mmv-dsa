
def gradingStudents(grades):
    for i in range(len(grades)):
        if grades[i] < 38:
            continue
        diff = abs((grades[i]%10)-10)
        if diff > 5:
            diff-=5
        
        if diff < 3:
            while grades[i]%10 != 5 and grades[i]%10 != 0:
                grades[i]+=1

    return grades


res = gradingStudents([73,
    67,
    38,
    33])

print(res)
