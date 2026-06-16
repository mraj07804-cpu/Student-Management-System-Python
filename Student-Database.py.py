class Exam:
    def __init__(self, roll_no, name, subjects_marks):
        self.roll_no = roll_no
        self.name = name
        self.subjects_marks = subjects_marks

    def total_marks(self):
        return sum(self.subjects_marks)

    def percentage(self):
        return self.total_marks() / len(self.subjects_marks)

    def grade(self):
        percent = self.percentage()
        if percent >= 90:
            return "A+"
        elif percent >= 75:
            return "A"
        elif percent >= 60:
            return "B"
        elif percent >= 50:
            return "C"
        else:
            return "Fail"

    def display(self):
        print("\nRoll No:", self.roll_no)
        print("Name:", self.name)
        print("Marks:", self.subjects_marks)
        print("Total:", self.total_marks())
        print("Percentage:", self.percentage())
        print("Grade:", self.grade())


class ExamDatabase:
    def __init__(self):
        self.records = []

    def add_record(self):
        roll_no = input("Enter Roll Number: ")
        name = input("Enter Name: ")
        marks_input = input("Enter marks (comma separated): ")

        marks = [int(m.strip()) for m in marks_input.split(",")]

        exam = Exam(roll_no, name, marks)
        self.records.append(exam)
        print("Record added successfully!")

    def display_all(self):
        if not self.records:
            print("No records found.")
        else:
            for record in self.records:
                record.display()

    def search_record(self):
        roll_no = input("Enter Roll Number to search: ")
        for record in self.records:
            if record.roll_no == roll_no:
                record.display()
                return
        print("Record not found.")

    def delete_record(self):
        roll_no = input("Enter Roll Number to delete: ")
        for record in self.records:
            if record.roll_no == roll_no:
                self.records.remove(record)
                print("Record deleted successfully!")
                return
        print("Record not found.")


# Main Menu
db = ExamDatabase()

while True:
    print("\n===== Exam Database Menu =====")
    print("1. Add Record")
    print("2. Display All Records")
    print("3. Search Record")
    print("4. Delete Record")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        db.add_record()
    elif choice == "2":
        db.display_all()
    elif choice == "3":
        db.search_record()
    elif choice == "4":
        db.delete_record()
    elif choice == "5":
        print("Exiting...")
        break
    else:
        print("Invalid choice!")
