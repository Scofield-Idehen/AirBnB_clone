Project Overview
The AirBnB Clone project aims to replicate the functionality of the popular AirBnB platform, allowing users to manage and interact with property listings through a command-line interface. The project is organized collaboratively using branches and pull requests on GitHub to streamline development.

Command Interpreter (Console)
Description
The command interpreter, or console, serves as the primary interface for users to interact with the AirBnB Clone system. It allows for the execution of various commands to manage property listings, user accounts, and more.

How to Start
To start the console, navigate to the project directory and run the following command in your terminal:

bash
Copy code
$ ./console.py
Usage
Once in interactive mode, you can use the following commands:

help: Display a list of documented commands.
quit: Exit the console.
Examples
Interactive Mode
bash
Copy code
$ ./console.py
(hbnb) help
Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) quit
$
Non-Interactive Mode
bash
Copy code
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
Running Tests
Ensure all tests pass in non-interactive mode by executing the following command:

bash
Copy code
$ echo "python3 -m unittest discover tests" | bash
