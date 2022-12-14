class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in (self.courses_in_progress + self.finished_courses) and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.finished_courses += ['Java']

cool_mentor = Lecturer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python', 'Java']

stern_reviewer = Reviewer("Ned", "Stark")
stern_reviewer.courses_attached += ['Python']

stern_reviewer.rate_hw(best_student, 'Python', 10)
stern_reviewer.rate_hw(best_student, 'Java', 7) # Не должно срабатывать
stern_reviewer.rate_hw(best_student, 'Python', 8)

best_student.rate_hw(cool_mentor, 'Python', 9)
best_student.rate_hw(cool_mentor, 'Java', 10)

print(best_student.grades)
print(cool_mentor.grades)