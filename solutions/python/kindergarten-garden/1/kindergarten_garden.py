class Garden:
    student_list = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fred', 'Ginny', 'Harriet', 'Ileana', 'Joseph', 'Kincaid', 'Larry']

    plant_mapping = {
        'G': 'Grass',
        'C': 'Clover',
        'R': 'Radishes',
        'V': 'Violets'
    }
    
    def __init__(self, diagram, students=None):
        self.diagram = diagram
        self.rows = self.diagram.split('\n')
        if students is None:
            self.students = sorted(Garden.student_list)
        else:
            self.students = sorted(students)

    def plants(self, student):
        plant_list = []
        student_idx = (self.students.index(student)) * 2
        for row in self.rows:
            plant_list.extend([row[student_idx], row[student_idx + 1]])
    
        return [Garden.plant_mapping[p] for p in plant_list]
                
    
