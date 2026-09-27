from student import Student


class StudentGradeCalculator:

    def __init__(self):
        self.student_list = []

    def add_student(self):
        name = input("\nEnter Student Name: ").strip()

        while not name:
            print("Name cannot be empty. Please try again.")
            name = input("Enter Student Name: ").strip()

        marks = []

        for subject in Student.SUBJECTS:
            while True:
                try:
                    mark = int(
                        input(f"Enter marks for {subject} (out of 100): ")
                    )

                    if 0 <= mark <= 100:
                        marks.append(mark)
                        break
                    else:
                        print("Invalid marks! Enter marks between 0 and 100.")

                except ValueError:
                    print("Invalid input! Please enter a valid integer.")

        student = Student(name, marks)
        self.student_list.append(student)

        print("\nResult saved successfully!")
        student.display_result()

    def display_all_students(self):
        print("\n====== ALL STUDENTS REPORT ======")

        if not self.student_list:
            print("No student records found.")
            return

        for student in self.student_list:
            student.display_result()

        print(f"\nTotal Students Entered: {len(self.student_list)}")

    def run(self):
        print("==================================")
        print("     STUDENT GRADE CALCULATOR")
        print("==================================")

        while True:
            self.add_student()

            choice = input("\nAdd another student? (yes/no): ").strip().lower()

            if choice != "yes":
                break

        self.display_all_students()

        print("\nThank you for using Student Grade Calculator!")


if __name__ == "__main__":
    calculator = StudentGradeCalculator()
    calculator.run()

