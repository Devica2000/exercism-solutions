class School:
    
    def __init__(self):
        self._grades = {}
        self._added = []

    def add_student(self, name, grade):
        all_students = []
        for grade_list in self._grades.values():
            for student in grade_list:
                all_students.append(student)
                
        if name in all_students:
            self._added.append(False)
        else:
            if grade in self._grades:
                self._grades[grade].append(name)
            else:
                self._grades[grade] = [name]
            self._added.append(True)
            
    def roster(self):
        all_students = []
        for grade in sorted(self._grades):
            all_students.extend(sorted(self._grades[grade]))
        return all_students

    def grade(self, grade_number):
        #if someone puts a grade number with no students
        #self._grade[grade_number] will throw a key error
        #use .get() instead
        return sorted(self._grades.get(grade_number, []))

    def added(self):
        return self._added
