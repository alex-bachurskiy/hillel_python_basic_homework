from group_limit_reached_exception_bachurskyi_hw_14 import GroupLimitReachedException


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
