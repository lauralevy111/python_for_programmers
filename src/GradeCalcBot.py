

pointsPossible = 100
studentName = input("Enter student name: ")
letterGrade = "ERROR"
percent = 0

def calcPercentGrade(score, pointsPossible):
    print("calculating grade")
    percent = round(score/pointsPossible,2)
    return percent

def calcLetterGrade(percent):

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
        letterGrade = "E"
    elif(.59 >= percent >= .50):
        letterGrade = "F"

    return letterGrade


try:
    score =float(input("Enter test score: "))
    print("score = {}".format(score))
    calcPercentGrade(score, pointsPossible)
    calcLetterGrade(calcPercentGrade(score,pointsPossibler))
except Exception:
    print("you need to enter a valid score")


print("Student = {} ".format(studentName))
print("\nLetterGrade = {} ".format(letterGrade))
print("\nPercentage score = {}".format(percent))
