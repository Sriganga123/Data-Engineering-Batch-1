def create_student_file():
    with open("student.txt", "w") as file:
        file.write("Name: Shivathmika\n")
        file.write("Age: 20\n")
        file.write("Marks:89\n")
        file.write("Grade: A\n")
def read_student_file():
    with open("student.txt", "r") as file:
        contents = file.read()
        print(contents)


create_student_file()
read_student_file()


