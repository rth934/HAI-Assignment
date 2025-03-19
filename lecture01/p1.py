class Student:
    def __init__(self,student_id,name,age):
        self.id=student_id
        self.name=name
        self.age=age
    def display_info(self):
        print("아이디:",self.id,"/ 이름:",self.name,"/ 나이:",self.age)

class StudentManager:
    def __init__(self):
        self.student=[]
    def add_student(self,student):
        self.student.append(student)
    def display_all_student(self):
        for student in self.student:
            student.display_info()


a=Student("1번","김철수","20살")
b=Student("2번","이영희","21살")
c=Student("3번","박지민","19살")

manager=StudentManager()
manager.add_student(a)
manager.add_student(b)
manager.add_student(c)


print("현재 등록된 학생 목록:")
manager.display_all_student()

d=Student("4번","한지수","22살")
manager.add_student(d)

print("학번 4번 학생 추가 후:")
manager.display_all_student()
