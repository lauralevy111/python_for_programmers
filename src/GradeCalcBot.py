
pointsPossible = 100
score = 98
studentName = "Laura"

"""
a= 100-90%
b= 89-80%
c= 79-70%
d= 69-70%
f= 59-0%
"""


percent = float(score/pointsPossible)
letterGrade = "TBD"

if (1.00 >= percent >= .90):
    letterGrade = "A"
elif(.89 >= percent >= .80):
    letterGrade = "B"
elif(.79 >= percent >= .70):
    letterGrade = "C"
elif(.69 >= percent >= .60):
    letterGrade = "D"
elif(.59 >= percent >= 0):
    letterGrade = "F"

print("LetterGrade = {}".format(letterGrade))
