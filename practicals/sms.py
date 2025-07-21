print("-----------------student management system----------------------")

class StudentManagement():
    def __init__(self, student_id, name, grade, marks):
        self.student_id = student_id
        self.name = name
        self.marks = marks
        self.grade = grade

    def display(self):
        print(self.student_id, self.name, self.grade, self.marks)
        return f"{self.student_id}, {self.name}, {self.grade}, {self.marks}"  #  Add return for print
    
    def __str__(self):
      return f"{self.student_id}, {self.name}, {self.grade}, {self.marks}"
        
class StudentManager():
    def __init__(self):
        self.students = []

    def add(self, student_id, name, grade, marks):
        for student in self.students:
            if student.student_id == student_id:
                print("studentid already exists")
                return "add failed"  

        new_students = StudentManagement(student_id, name, grade, marks)
        self.students.append(new_students)
        print(new_students, "added successfully")
        return "Student added" 

    def update(self, student_id, name='none', grade='none', marks='none'):
        for student in self.students:
            if student.student_id == student_id:
                if name != 'none':
                    student.name = name
                if grade != 'none':
                    student.grade = grade
                if marks != 'none':
                    student.marks = marks
                print("update successfully")
                return "Update done" 

        print("student not found")
        return "Update failed: Not found" 
    def delete(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                print("deleted successfully")
                return "delete done"
          
            else:
                print("student not found")
                return "Delete failed: Not found" 
            
    def display(self):
     print(f"student_id:{student_id}\n, name:{name} \n, marks:{marks},grade:{grade}" )

print("-----------------student detail----------------------")
# print(
#     f"NOTE:,\n"
#     f"A.student_id should contain alphabet with numbers and underscores,\n"
#     f"B. It should be in small letters,\n"
#     f"like abc_123"
# )
# while True:
#  student_id=input("Enter student_id:")
#  if(student_id.islower())and any(char.isnumeric() for char in student_id) and any( not char.isalnum() for char in student_id):
#      print("valid studentid")
#      break
#  else:
#     print("invalid student id")

# while True:
#  name = input("Enter your name: ")
#  if name.isalpha() and 3 <= len(name) <= 20:
#      print(" Valid name")
#      break
#  else:
#      print("Invalid name")
# while True:
#  marks = float(input("Enter marks: "))
#  grade3=(marks)
#  if 80 < marks <= 100:
#     print("grade = O")
#  elif 70 < marks <= 80:
#     print("grade = A")
#  elif 60 < marks <= 70:
#     print("grade = B")
#  elif 50 <= marks <= 60:
#     print("grade = C")
#  elif 40 <= marks < 50:
#     print("grade = D")
#  elif 30 <= marks < 40:
#     print("grade = E")
#  else:
#     print("grade = FAIL")
#  break
val = StudentManagement("kanika_123","kanika thakur","A",91)
print("Student detail:", val.display())

print("-----------------add student----------------------")
val2=StudentManager()
print(
    f"NOTE:,\n"
    f"A.student_id should contain alphabet with numbers and underscores,\n"
    f"B. It should be in small letters,\n"
    f"like abc_123"
)
while True:
 student_id=input("Enter student_id:")
 if(student_id.islower())and any(char.isnumeric() for char in student_id) and any( not char.isalnum() for char in student_id):
     print("valid studentid")
     break
 else:
    print("invalid student id")

while True:
 name= input("Enter your name: ")
 if name.isalpha() and 3 <= len(name) <= 20:
     print(" Valid name")
     break
 else:
     print("Invalid name")


while True:
 marks=float(input("Enter marks:"))
 grade =(marks)
 if 80 < marks <= 100:
    print("grade = O")
 elif 70 < marks <= 80:
    print("grade = A")
 elif 60 < marks <= 70:
    print("grade = B")
 elif 50 <= marks <= 60:
    print("grade = C")
 elif 40 <= marks < 50:
    print("grade = D")
 elif 30 <= marks < 40:
    print("grade = E")
 else:
    print("grade = FAIL")
 break
print("Add student:", val2.add(student_id,name,grade,marks))

print("-----------------update student----------------------")
print(
    f"NOTE:,\n"
    f"A.student_id should contain alphabet with numbers and underscores,\n"
    f"B. It should be in small letters,\n"
    f"like abc_123"
)
while True:
 student_id=input("Enter student_id:")
 if(student_id.islower())and any(char.isnumeric() for char in student_id) and any( not char.isalnum() for char in student_id):
     print("valid studentid")
     break
 else:
    print("invalid student id")

while True:
 name= input("Enter your name: ")
 if name.isalpha() and 3 <= len(name) <= 20:
     print(" Valid name")
     break
 else:
     print("Invalid name")

while True:
 marks=float(input("Enter marks:"))
 grade=(marks)
 if 80 < marks<= 100:
    print("grade = O")
 elif 70 < marks<= 80:
    print("grade = A")
 elif 60 < marks<= 70:
    print("grade = B")
 elif 50 <= marks<= 60:
    print("grade = C")
 elif 40 <= marks< 50:
    print("grade = D")
 elif 30 <= marks< 40:
    print("grade = E")
 else:
    print("grade = FAIL")
 break
print("Update student info:", val2.update(student_id,name,grade,marks))

print("-----------------delete student----------------------")
name=input("Enter name you want to delete:")
print("Delete student:", val2.delete(name))


