
class Student:
    SUBJECTS = ["Maths", "Physics", "Chemistry", "English", "Computer"]

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        self.total = self.calculate_total()
        self.percentage = self.calculate_percentage()
        self.grade = self.calculate_grade()

    def calculate_total(self):
        return sum(self.marks)

    def calculate_percentage(self):
        return (self.total / 500) * 100

    def calculate_grade(self):
        if self.percentage >= 90:
            return "A+"
        elif self.percentage >= 80:
            return "A"
        elif self.percentage >= 70:
            return "B"
        elif self.percentage >= 60:
            return "C"
        elif self.percentage >= 50:
            return "D"
        else:
            return "F - Fail"

    def display_result(self):
        print("\n==================================")
        print(f"Student Name  : {self.name}")
        print("Marks         :")

        for subject, mark in zip(self.SUBJECTS, self.marks):
            print(f"  {subject:<12}: {mark}")

        print("----------------------------------")
        print(f"Total         : {self.total} / 500")
        print(f"Percentage    : {self.percentage:.2f} %")
        print(f"Grade         : {self.grade}")
        print("==================================")
