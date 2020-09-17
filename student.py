class Student:
    def __init__(self, name, gender, matric_number, department):
        self.name = name
        self.gender = gender
        self.matric_number = matric_number
        self.department = department
        self.subjects = []

    # Properties
    def get_name(self):
        return self.name

    def get_gender(self):
        return self.gender

    def get_matric_number(self):
        return self.matric_number

    def get_department(self):
        return self.department

    def get_subjects(self):
        return self.subjects

    #Methods
    def add_subject(self, subject):
        self.subjects.append({"subject": subject, "score": 0 })
