#50. [Interactive Coding Exercise] High Score

'''
You are going to write a program that calculates the highest score from a List of scores.
e.g. student_scores = [78, 65, 89, 86, 55, 91, 64, 89]
Important you are not allowed to use the max or min functions. The output words must match the example. i.e
    The highest score in the class is: x
'''
# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
import random
#https://en.wikipedia.org/wiki/SAT#Percentiles_for_total_scores_(2019)

students_SAT = [random.randint(400,1600) for i in range(99)]

for score in students_SAT:
    student_scores.append(score)


max_score = 0
min_score = 999

for score in student_scores:
    if score >= max_score:
        max_score = score
    if score <= min_score:
        min_score = score

print(f"The highest score i the clas is: {max_score}")
print(f"The lowest score in the class is:{min_score}")

print("-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-")
print("The lazy man try:")
print("-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-")
print(f"The highest score in the class is:{max(student_scores)}")
print(f"The lowes score is the class is:{min(student_scores)}")