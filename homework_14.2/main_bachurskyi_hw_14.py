from student_bachurskyi_hw_14 import Student
from group_bachurskyi_hw_14 import Group
from group_limit_reached_exception_bachurskyi_hw_14 import GroupLimitReachedException


def main():
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




if __name__ == '__main__':
    main()
