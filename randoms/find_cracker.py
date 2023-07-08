def find_hack(record):
  grade_points = {
        "A": 30,
        "B": 20,
        "C": 10,
        "D": 5
    }
  def has_additional_points(grades):
    if len(grades) < 5:
      return False
    
    if all([True if g in ["A","B"] else False for g in grades ]) == False:
      return False
    
    return True
  
  
    
  hackers = []
  
  for i in range(len(record)):
    
    name = record[i][0]
    score_given = record[i][1]
    grades = record[i][2]

    if score_given > 200:
      print(f"{name} is hacker because score given is greate than 200")
      hackers.append(name)
      continue

    print(record[i])

    total_grades_score = 0

    for g in grades:
      try:
        total_grades_score += grade_points[g]
      except:
        continue


    if total_grades_score > 200:
      print(f"{name} is hacker because total grades score greater than 200 - {total_grades_score}")
      hackers.append(name)
      continue

    hap = has_additional_points(grades)
    if hap:
      total_grades_score += 20
      if total_grades_score > 200 and score_given == 200:
        continue 
      elif total_grades_score > 220 and score_given == 200:
        hackers.append(name)
        continue

    if total_grades_score != score_given:
      print(f"{name} not equal to score gien {total_grades_score}")
      hackers.append(name)
    
  return hackers
    
      





    

    



array = [
        ["name1", 150, ["B", "A", "A", "C", "A", "A"]],
        ["name2", 120, ["B", "A", "A", "A"]],
        ["name3", 160, ["B", "A", "A", "A","A"]],
        ["name4", 140, ["B", "A", "A", "C", "A"]]
    ]

print(find_hack(array))