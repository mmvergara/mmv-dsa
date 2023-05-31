def calculate_score(record):
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

    total_grades_score = sum([grade_points[g] for g in grades])

    if total_grades_score > 200:
      hackers.append(name)
      print(f"Found hacker {name}")
      continue

    if has_additional_points(grades):




    

    



array = [
  ["name1", 445, ["B", "A", "A", "C", "A", "A"]],
  ["name2", 110, ["B", "A", "A", "A"]],
  ["name3", 200, ["B", "A", "A", "C"]],
  ["name4", 200, ["A", "A", "A", "A", "A", "A", "A"]]
]
print(calculate_score(array))