""" Functions to help calculate GPAs. """

def GPA(courses):
  """ Courses is a list of (credits, grade) pairs. """
  lookup_grade = {'S': 10
                 ,'A': 9
                 ,'B': 8
                 ,'C': 7
                 ,'D': 6
                 ,'E': 4
                 ,'F': 0}
  credits = sum([a for (a, b) in courses])
  grade_points = sum([a * lookup_grade[b] for (a, b) in courses])

  return grade_points/float(credits)
