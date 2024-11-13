class Student:
    def __init__(self, student_id, name, score):
        self.student_id = student_id
        self.name = name
        self.score = score

    def __str__(self):
        return f"ID: {self.student_id}, Name: {self.name}, Score: {self.score}"


# Create three student objects
student1 = Student(1, "Devin", 85)
student2 = Student(2, "Justin", 92)
student3 = Student(3, "Chellshe", 92)

# Store them in a list
students = [student1, student2, student3]

# Find the highest score
highest_score = max(student.score for student in students)

# Print students with the highest score
print("Student(s) with the highest score:")
for student in students:
    if student.score == highest_score:
        print(student)