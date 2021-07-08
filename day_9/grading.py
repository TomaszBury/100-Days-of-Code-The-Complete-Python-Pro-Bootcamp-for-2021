import os
def clear(): os.system('cls') #on Windows System
clear()
'''
Instructions
You have access to a database of student_scores in the format of a dictionary. The keys in student_scores are the names of the students and the values are their exam scores.
Write a program that converts their scores to grades. By the end of your program, you should have a new dictionary called student_grades that should contain student names for keys and their grades for values. The final version of the student_grades dictionary will be checked.
DO NOT modify lines 1-7 to change the existing student_scores dictionary.
DO NOT write any print statements.
This is the scoring criteria:
    Scores 91 - 100: Grade = "Outstanding"
    Scores 81 - 90: Grade = "Exceeds Expectations"
    Scores 71 - 80: Grade = "Acceptable"
    Scores 70 or lower: Grade = "Fail"
'''
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇
def grading(student_score):
    if student_score >= 91:
        return "Outstanding"
    elif student_score >= 81:
        return "Exceeds Expectations"
    elif student_score >= 71:
        return "Acceptable"
    else:
        return "Fail"

for key in student_scores:
    student_grades[key] = grading(student_scores[key])
'''    
for key in student_grades:
    print(f"{key}:{student_grades[key]}")
'''
# 🚨 Don't change the code below 👇
print(student_grades)