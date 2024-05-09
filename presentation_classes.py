# ------------------------------------------------------------------------------- #
# Title: Presentation Classes Module
# # Description: A collection of presentation classes for managing the application
# ChangeLog: (Who, When, What)
# RRoot,1.5.2030,Created Script
# ------------------------------------------------------------------------------- #

try:
    if __name__ == "__main__":
        raise Exception("Please use the main.py file to start this application.")
    # else:
    #     import data_classes as data
except Exception as e:
    print(e.__str__())


class IO:
    """
    A collection of presentation layer functions that manage user input and output

    ChangeLog: (Who, When, What)
    RRoot,1.1.2030,Created Class
    RRoot,1.2.2030,Added menu output and input functions
    RRoot,1.3.2030,Added a function to display the data
    RRoot,1.4.2030,Added a function to display custom error messages
    RRoot,1.5.2030,Converted methods to use student objects instead of dictionaries
    """
    pass

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """ This function displays the a custom error messages to the user

        ChangeLog: (Who, When, What)
        RRoot,1.3.2030,Created function

        :param message: string with message data to display
        :param error: Exception object with technical message to display

        :return: None
        """

        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def output_menu(menu: str):
        """ This function displays the menu of choices to the user

        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created function

        :return: None
        """
        print()
        print(menu)
        print()

    @staticmethod
    def input_menu_choice():
        """ This function gets a menu choice from the user

        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created function

        :return: string with the users choice
        """
        choice = "0"
        try:
            choice = input("Enter your menu choice number: ")
            if choice not in ("1", "2", "3", "4"):  # Note these are strings
                raise Exception("Please, choose only 1, 2, 3, or 4")
        except Exception as e:
            IO.output_error_messages(e.__str__())  # passing the exception object to avoid the technical message

        return choice

    @staticmethod
    def output_letter_by_gpa(student_data: list):
        """ This function displays the letter grades base on their GPA to the user

        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created function
        RRoot,1.2.2030,Converted code to use student objects instead of dictionaries

        :param student_data: list of student object data to be displayed

        :return: None
        """
        print()
        print("-" * 50)
        for student in student_data:
            if student.gpa >= 4.0:
                message = " {} {} earned an A with a {:.2f} GPA"
            elif student.gpa >= 3.0:
                message = " {} {} earned a B with a {:.2f} GPA"
            elif student.gpa >= 2.0:
                message = " {} {} earned a C with a {:.2f} GPA"
            elif student.gpa >= 1.0:
                message = " {} {} earned a D with a {:.2f} GPA"
            else:
                message = " {} {}'s {:.2f} GPA was not a passing grade"

            print(message.format(student.first_name, student.last_name, student.gpa))
        print("-" * 50)

    @staticmethod
    def input_student_data(student_data: list, student_type: object):  # TODO: Create a Student parameter (Done)
        """ This function gets the first name, last name, and GPA from the user

        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created function
        RRoot,1.2.2030,Converted code to use student objects instead of dictionaries

        :param student_data: list of student rows to be filled with input data
        :param student_type: A reference to data_class.Student use to create a Student object

        :return: list
        """

        try:
            # Input the data
            # student = data.Student()  # TODO: Remove the direct dependency to data_classes (Done)
            student = student_type()
            student.first_name = input("What is the student's first name? ")
            student.last_name = input("What is the student's last name? ")
            student.gpa = float(input("What is the student's GPA? "))
            student_data.append(student)

        except ValueError as e:
            IO.output_error_messages("That value is not the correct type of data!", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        return student_data
