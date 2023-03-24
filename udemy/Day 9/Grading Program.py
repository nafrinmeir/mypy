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

for key in student_scores:
        #print(key)
        #print(student_scores[key])
    if student_scores[key] >= 91 and student_scores[key] < 100:
        student_grades[key] = "Outstanding"
        #print("Outstanding")
    elif student_scores[key] >= 81 and student_scores[key] < 90:
        student_grades[key] = "Exceeds Expectations"
        #print("Exceeds Expectations")
    elif student_scores[key] >= 71 and student_scores[key] < 80:
        student_grades[key] = "Acceptable"
        #print("Acceptable")
    else:
        student_grades[key] = "Fail"
        #print("Fail")


# 🚨 Don't change the code below 👇
print(student_grades)





#This is the scoring criteria:
#Scores 91 - 100: Grade = "Outstanding"
#Scores 81 - 90: Grade = "Exceeds Expectations"
#Scores 71 - 80: Grade = "Acceptable"
#Scores 70 or lower: Grade = "Fail"