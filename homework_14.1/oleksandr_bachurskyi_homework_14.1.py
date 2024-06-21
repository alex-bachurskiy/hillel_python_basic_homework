# ДЗ 14.1. Виняток користувача
# Модифікуйте клас Група (завдання минулої лекції) так, щоб при спробі додавання до групи більше 10-ти студентів,
# було порушено виняток користувача.
# Таким чином потрібно створити ще й виняток користувача для цієї ситуації. І обробити його поза межами класу.
# Тобто. потрібно перехопити цей виняток, при спробі додавання 11-го студента

class GroupLimitReachedException(Exception):
    def __init__(self, error_message, group_name):
        self.error_message = error_message
        self.group_name = group_name


class Human:
    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f'{self.first_name} {self.last_name}, {self.age} years old, {self.gender}'


class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return super().__str__() + f' {self.record_book}'

    def show_info(self):
        print(f"Name: {self.first_name} has {self.record_book}")


class Group:

    def __init__(self, number, student_limit=10):
        self.number = number
        self.group = set()
        self.student_limit = student_limit

    def add_student(self, student):
        if len(self.group) == self.student_limit:
            raise GroupLimitReachedException(f"Limit of {self.student_limit} "
                                             f"students per group reached", self.number)
        self.group.add(student)

    def delete_student(self, last_name):
        student_to_remove = self.find_student(last_name)
        if student_to_remove:
            self.group.remove(student_to_remove)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        all_students = '\n'.join(str(student) for student in self.group)
        return f'Group Number: {self.number}\n{all_students}'


st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
st3 = Student('Male', 28, 'John', 'Smith', 'AN138')
st4 = Student('Female', 22, 'Emily', 'Johnson', 'AN143')
st5 = Student('Male', 27, 'Michael', 'Brown', 'AN146')
st6 = Student('Female', 24, 'Emma', 'Williams', 'AN139')
st7 = Student('Male', 29, 'Daniel', 'Miller', 'AN144')
st8 = Student('Female', 26, 'Olivia', 'Martinez', 'AN137')
st9 = Student('Male', 31, 'James', 'Davis', 'AN140')
st10 = Student('Female', 23, 'Sophia', 'Garcia', 'AN147')
st11 = Student('Male', 32, 'David', 'Wilson', 'AN141')

gr = Group('PD1')

try:
    gr.add_student(st1)
    gr.add_student(st2)
    gr.add_student(st3)
    gr.add_student(st4)
    gr.add_student(st3)
    gr.add_student(st4)
    gr.add_student(st5)
    gr.add_student(st6)
    gr.add_student(st7)
    gr.add_student(st8)
    gr.add_student(st9)
    gr.add_student(st10)
    gr.add_student(st11)

    print(gr)

except GroupLimitReachedException as error:
    print(error)
except Exception as error:
    print(error)
