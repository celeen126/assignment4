GitHub: https://github.com/celeen126/assignment4
DockerHub: https://hub.docker.com/r/celeenqassem/studentapp/tags

This Python app implements a basic student management system with features for adding students, searching for student details, updating student information (name, age, CGPA), deleting students, and displaying a list of all students. It utilizes the `tabulate` library to present student information in a tabulated format. The script provides a menu-driven interface, allowing users to interact with and manage student records through a series of prompts and actions.

Usage:
1. Install `tabulate` for the displaying of records in form to tables.
2. Write the following command in command prompt:
    python ./main.py
3. Follow the menu prompts to perform actions such as adding, searching, updating, or deleting student records.

OR

1. Have an active docker environment running on the system
2. Pull the image from dockerhub using the following command:
    docker pull celeenqassem/studentapp:v1.0
3. Write the following command:
    docker run -i -t celeenqassem/studentapp:v1.0
4. Follow the menu prompts to perform actions such as adding, searching, updating, or deleting student records.

Features:
- Add Student: Collects information (Roll No, Name, Age, CGPA) and adds a student to the system.
- Search Details: Searches for a student based on Roll No and displays their information.
- Update Name, Age, CGPA: Allows updating the information of a specific student.
- Delete: Removes a student from the system based on their Roll No.
- Show All Students: Displays a tabulated view of all students in the system.
- Exit: Terminates the program.