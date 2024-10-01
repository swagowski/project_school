class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades_student = {}

    def __str__(self):
        return f" Имя: {self.name} Фамилия: {self.surname} Среднее оценка за домашние задания: {self.grades_student} Курсы в процессе изучения: {self.courses_in_progress} Завершенные курсы: {self.finished_courses}"


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades_lecturer = {}

    def __str__(self):
        return f"Имя: {self.name} Фамилия: {self.surname} Средняя оценка за лекции: {self.grades_lecturer}"


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        return f"Имя: {self.name} Фамилия: {self.surname}"

    def rate_student(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades_student:
                student.grades_student[course] += [grade]
            else:
                student.grades_student[course] = [grade]
        else:
            return 'Ошибка'

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_attached and course in lecturer.courses_attached:
            if course in lecturer.grades_lecturer:
                lecturer.grades_lecturer[course] += [grade]
            else:
                lecturer.grades_lecturer[course] = [grade]
        else:
            return 'Ошибка'


# average_students_grades = fmean(self.grades_student['Git','Python'])


best_student = Student('sam', 'nikitin', 'male')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']
best_student.finished_courses += ['Введение в программирование']
cool_lecturer = Lecturer('John', 'Jhonson')
cool_lecturer.courses_attached += ['Python']
cool_lecturer.courses_attached += ['Git']
cool_lecturer.grades_lecturer['Python'] = [10, 10, 10, 10, 10]
cool_lecturer.grades_lecturer['Git'] = [10, 10, 10, 10, 9]
cool_reviewer = Reviewer('Alex', 'Vibe')
cool_reviewer.courses_attached += ['Python']
cool_reviewer.courses_attached += ['Git']
cool_reviewer.rate_student(best_student, 'Python', 10)
cool_reviewer.rate_student(best_student, 'Python', 9)
cool_reviewer.rate_student(best_student, 'Git', 7)
cool_reviewer.rate_student(best_student, 'Git', 8)

# avarage_students_grades=float(sum(best_student.grades_student.get(['Git']))/len(best_student.grades_student.get(['Git'])))

print(cool_reviewer)
print(cool_lecturer)
print(best_student)
