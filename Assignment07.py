# ------------------------------------------------- #
# Title: Assignment07
# Desc: This assignment demonstrates using data classes
# with structured error handling
# ChangeLog: (Who, When, What)
# Rakshit Govil,11/21/2024,Created Script
# Rakshit Govil,11/21/2024,Converted dictionary rows to student class objects.
# Rakshit Govil,11/21/2024,Added properties and private attributes
# ------------------------------------------------- #
import json

# Data -------------------------------------------- #
FILE_NAME: str = 'Enrollments.json'
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course
    2. Show current data  
    3. Save data to a file
    4. Exit the program
----------------------------------------- 
'''

students: list = []  # a table of student data
menu_choice = ''


class Person:
    """
    A class representing a person with basic name information.

    Attributes:
        first_name (str): The first name of the person.
        last_name (str): The last name of the person.

    Methods:
        first_name: Getter and setter for the first name of the person.
        last_name: Getter and setter for the last name of the person.
        __str__: Returns a string representation of the person's full name.

    """

    def __init__(self, first_name: str = '', last_name: str = ''):
        """
        Initializes a Person object with the given first and last name.

        :param first_name: The first name of the person (default is an empty string).
        :param last_name: The last name of the person (default is an empty string).
        """
        self.first_name = first_name
        self.last_name = last_name

    @property
    def first_name(self):
        """
        Getter for the first name.

        :return: The first name, formatted with title case.
        """
        return self.__first_name.title()

    @first_name.setter
    def first_name(self, value: str):
        """
        Setter for the first name. Ensures the name consists of alphabetic characters or is an empty string.

        :param value: The value to set the first name to.
        :raises ValueError: If the value contains non-alphabetic characters (except an empty string).
        """
        if value.isalpha() or value == "":
            self.__first_name = value
        else:
            raise ValueError("The first name should not contain numbers.")

    @property
    def last_name(self):
        """
        Getter for the last name.

        :return: The last name, formatted with title case.
        """
        return self.__last_name.title()

    @last_name.setter
    def last_name(self, value: str):
        """
        Setter for the last name. Ensures the name consists of alphabetic characters or is an empty string.

        :param value: The value to set the last name to.
        :raises ValueError: If the value contains non-alphabetic characters (except an empty string).
        """
        if value.isalpha() or value == "":
            self.__last_name = value
        else:
            raise ValueError("The last name should not contain numbers.")

    def __str__(self):
        """
        Returns a string representation of the person's full name.

        :return: A string in the format "FirstName,LastName".
        """
        return f'{self.first_name},{self.last_name}'


class Student(Person):
    """
    A class representing a student, which extends from Person to include course enrollment details.

    Attributes:
        first_name (str): The first name of the student (inherited from Person).
        last_name (str): The last name of the student (inherited from Person).
        course_name (str): The course the student is enrolled in.

    Methods:
        course_name: Getter and setter for the course name.
        __str__: Returns a string representation of the student's full name and enrolled course.
    """

    def __init__(self, first_name: str = '', last_name: str = '', course_name: str = ''):
        """
        Initializes a Student object with the given name and course.

        :param first_name: The first name of the student (default is an empty string).
        :param last_name: The last name of the student (default is an empty string).
        :param course_name: The course the student is enrolled in (default is an empty string).
        """
        super().__init__(first_name=first_name, last_name=last_name)
        self.course_name = course_name

    @property
    def course_name(self):
        """
        Getter for the course name.

        :return: The course name.
        """
        return self.__course_name

    @course_name.setter
    def course_name(self, value: float):
        try:  # using a try block to capture when an input cannot be changed to a float
            self.__course_name = value
        except ValueError:
            raise ValueError("Course Name must be a combination of numeric value and alphabets")

    def __str__(self):
        """
        Returns a string representation of the student's full name and the course they are enrolled in.

        :return: A string in the format "FirstName,LastName,CourseName".
        """
        return f'{self.first_name},{self.last_name},{self.course_name}'


class FileProcessor:
    """
    A class to handle file operations related to student data, including reading and writing to JSON files.

    Methods:
        read_data_from_file: Reads student data from a JSON file and loads it into a list of Student objects.
        write_data_to_file: Writes student data from a list of Student objects to a JSON file.
    """

    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """
        Reads student data from a JSON file and appends the data as Student objects to a list.

        :param file_name: The name of the file to read from.
        :param student_data: The list to append the Student objects to.
        :return: The updated list of Student objects.
        """
        try:
            with open(file_name, "r") as file:
                list_of_dictionary_data = json.load(file)
                for student in list_of_dictionary_data:
                    student_object = Student(first_name=student["FirstName"],
                                              last_name=student["LastName"],
                                              course_name=student["CourseName"])
                    student_data.append(student_object)
        except FileNotFoundError as e:
            IO.output_error_messages("Text file must exist before running this script!", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        return student_data

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """
        Writes student data from a list of Student objects to a JSON file.

        :param file_name: The name of the file to write to.
        :param student_data: The list of Student objects to be written to the file.
        :return: None
        """
        try:
            list_of_dictionary_data = []
            for student in student_data:
                student_json = {"FirstName": student.first_name,
                                "LastName": student.last_name,
                                "CourseName": student.course_name}
                list_of_dictionary_data.append(student_json)

            with open(file_name, "w") as file:
                json.dump(list_of_dictionary_data, file, indent=4)
        except TypeError as e:
            IO.output_error_messages("Please check that the data is a valid JSON format", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)


class IO:
    """
    A class to handle all user input and output operations, including displaying menus, reading input,
    and showing student data.

    Methods:
        output_error_messages: Displays an error message to the user.
        output_menu: Displays the main menu of options to the user.
        input_menu_choice: Gets the user's menu choice.
        output_student_courses: Displays the list of students and their enrolled courses.
        input_student_data: Prompts the user for new student data and appends it to the list of students.
    """

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """
        Displays an error message to the user, optionally including technical details.

        :param message: The message to display to the user.
        :param error: An optional exception that provides technical details (default is None).
        :return: None
        """
        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def output_menu(menu: str):
        """
        Displays the main menu to the user.

        :param menu: The menu string to be displayed.
        :return: None
        """
        print(menu)

    @staticmethod
    def input_menu_choice():
        """
        Prompts the user to choose an option from the menu and validates the input.

        :return: The user's menu choice as a string.
        """
        choice = "0"
        try:
            choice = input("Enter your menu choice number: ")
            if choice not in ("1", "2", "3", "4"):
                raise Exception("Please, choose only 1, 2, 3, or 4")
        except Exception as e:
            IO.output_error_messages(e.__str__())

        return choice

    @staticmethod
    def output_student_courses(student_data: list):
        """
        Outputs a list of students and the courses they are enrolled in.

        :param student_data: The list of Student objects to be displayed.
        :return: None
        """
        print("-" * 50)
        for student in student_data:
            message = "Student {} {} is enrolled in {}"
            print(message.format(student.first_name, student.last_name, student.course_name))
        print("-" * 50)

    @staticmethod
    def input_student_data(student_data: list):
        """
        Prompts the user for student information (first name, last name, and course name) and
        appends the data as a new Student object to the provided list.

        :param student_data: The list to append the new Student object to.
        :return: The updated list of students.
        """
        try:
            student = Student()
            student.first_name = input("What is the student's first name? ")
            student.last_name = input("What is the student's last name? ")
            student.course_name = input("What is the student's Course Name? ")
            student_data.append(student)
        except ValueError as e:
            IO.output_error_messages("That value is not the correct type of data!", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        return student_data


# Main Body
students = FileProcessor.read_data_from_file(file_name=FILE_NAME, student_data=students)

while True:
    IO.output_menu(menu=MENU)

    menu_choice = IO.input_menu_choice()

    if menu_choice == "1":
        students = IO.input_student_data(student_data=students)
        continue

    elif menu_choice == "2":
        IO.output_student_courses(student_data=students)
        continue

    elif menu_choice == "3":
        FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=students)
        continue

    elif menu_choice == "4":
        break
    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")