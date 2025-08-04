class School:
    def __init__(self):
        self.grades = {}
        self.is_added = []
        self.already_added = set()

    def add_student(self, name, grade):
        grade_list: list = self.grades.setdefault(grade, [])

        if name in self.already_added:
            self.is_added.append(False)
        else:
            self.is_added.append(True)
            self.already_added.add(name)
            grade_list.append(name)

    def roster(self):
        result = []
        for grade in sorted(self.grades):
            result += sorted(self.grades[grade])

        return result

    def grade(self, grade_number):
        return sorted(self.grades.get(grade_number, []))

    def added(self):
        return self.is_added
