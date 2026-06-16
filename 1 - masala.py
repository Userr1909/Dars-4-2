# 1-masala.  Talabalar tizimi
# class Student:
# Properties:
# 	name string
# 	student_id string
# 	__grades list (private)
# Methods
# 	__init__(self, name: str, student_id: str) -> None
# 	add_grade(self, grade: int) -> None - Baho qo'shadi (0-100 oralig'ida bo'lishi kerak).
# 	calculate_average(self) -> float - Baholar o'rtachasini hisoblaydi.
# 	get_status(self) -> str - O'rtacha bahoga qarab statusni qaytaradi:
# 		90-100: A'lo
# 		80-89: Yaxshi
# 		70-79: Qoniqarli
# 		<70: Qoniqarsiz
# Klassdan foydalanish:
# student = Student("Nodira", "S123")
# # Yangi talaba yaratildi: Nodira, ID: S123, boshlang'ich baholar ro'yxati bo'sh.
# student.add_grade(85)
# # 85 bahosi qo'shildi.
# student.add_grade(90)
# # 90 bahosi qo'shildi.
# print(student.calculate_average())  # 87.5
# print(student.get_status())  # Yaxshi
# student.add_grade(150)  # Xato: Noto'g'ri baho

# Chiqish natijasi:
# 87.5
# Yaxshi
# Xato: Noto'g'ri baho
import os
os.system("cls")

class Student:
    def __init__(self, n, i):
        self.name = n
        self.student_id = i
        self.__grades = []

    def add_grade(self,grade):
        if grade < 0 or grade > 100:
            print("Xato: Noto'g'ri baho")
        else:
            self.__grades.append(grade)
        
    def calculate_average(self):
        return sum(self.__grades) / len(self.__grades)
    
    def get_status(self):
        ortacha = self.calculate_average()

        if ortacha >= 90:
            return "A'lo"
        elif ortacha >= 80:
            return "Yaxshi"
        elif ortacha >= 70:
            return "Qoniqarli"
        else:
            return "Qoniqarsiz"
        
student = Student("Nodira", "S123")
student.add_grade(85)
student.add_grade(90)

print(student.calculate_average())
print(student.get_status())       
student.add_grade(150)
# tayyor        