# 2-masala. Xodimlar tizimi
# Klass: Employee
# Properties:
# 	name: str - xodimning ismi
# 	employee_id: str - xodimning ID raqami
# 	__working_hours: list[int] â€” xodimning kunlik ishlagan soatlari (private)
# 	hourly_rate: float - soatlik ish haqi (default qiymat 15.0)
# Methods:
# 	__init__(self, name: str, employee_id: str, hourly_rate: float = 15.0) -> None
#  	Yangi xodimni yaratadi, ishlagan soatlar ro'yxatini bo'sh qiladi va soatlik ish haqini belgilaydi.

# 	log_hours(self, hour: int) -> bool
#  	Kunlik ishlagan soatlarni ro'yxatga qo'shadi.
#  	Soat 0 dan 24 gacha bo'lishi kerak.
#  	Noto'g'ri qiymat kiritilsa False qaytaradi, aks holda True.

# 	total_hours(self) -> int
#  	Barcha kunlik ishlagan soatlarning yig'indisini qaytaradi.

# 	calculate_salary(self) -> float
#  	Ishlagan umumiy soatlar va soatlik stavka asosida oylik maoshni hisoblaydi va qaytaradi.

# 	reset_hours(self) -> None
#  	Ishlangan soatlar ro'yxatini tozalaydi.

# Namuna:
# employee = Employee("Javlon", "E101", hourly_rate=20.0)

# print(employee.log_hours(8))   	# True
# print(employee.log_hours(9))   	# True
# print(employee.log_hours(10))  	# True
# print(employee.log_hours(25))  	# False 

# print(employee.total_hours())       	# 27
# print(employee.calculate_salary())  	# 540.0 (27 * 20)

# employee.reset_hours()
# print(employee.total_hours())       	# 0
# print(employee.calculate_salary())  	# 0.0

# Kutilayotgan natija:
# True
# True
# True
# False
# 27
# 540.0
# 0
# 0.0
import os
os.system("cls")

class Employee:
    def __init__(self, name, employee_id, hourly_rate = 15.0):
        self.name = name
        self.employee_id = employee_id
        self.__working_hours = []
        self.hourly_rate = hourly_rate

    def log_hours(self, hour):
        if hour < 0 or hour > 24:
            return False
        else:
            self.__working_hours.append(hour)
            return True

    def total_hours(self):
        return sum(self.__working_hours)

    def calculate_salary(self):
        return self.total_hours() * self.hourly_rate

    def reset_hours(self):
        self.__working_hours = []
employee = Employee("Javlon", "E101", hourly_rate=20.0)

print(employee.log_hours(8))
print(employee.log_hours(9))
print(employee.log_hours(10))
print(employee.log_hours(25))

print(employee.total_hours())
print(employee.calculate_salary())

employee.reset_hours()
print(employee.total_hours())
print(employee.calculate_salary())
# tayyor