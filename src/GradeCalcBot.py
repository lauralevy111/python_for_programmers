
pointsPossible = 100
studentName = input("Enter student name: ")
score =float(input("Enter test score: "))

#print(type (score)) # this line will print the type of var score


percent = round(score/pointsPossible,2)
letterGrade = "ERROR"

'''
a= 100-90%
b= 89-80%
c= 79-70%
d= 69-70%
f= 59-0%
'''
if (1.00 >= percent >= .90):
    letterGrade = "A"
elif(.89 >= percent >= .80):
    letterGrade = "B"
elif(.79 >= percent >= .70):
    letterGrade = "C"
elif(.69 >= percent >= .60):
    letterGrade = "D"
elif(.59 >= percent >= .50):
    letterGrade = "F"

print("Student = {} \nLetterGrade = {} \nPercentage score = {}".format(studentName,letterGrade,percent))
