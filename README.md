
# AirBnB Clone

This repository contains an implementation of the AirBnB clone project. The goal of this project is to recreate the functionality of the popular AirBnB platform, allowing users to manage and interact with property listings through a command-line interface.

## Project Description

The AirBnB clone project is divided into several phases:

1. **Console:** The first phase of the project focuses on creating a command-line interface (CLI) for managing objects related to the AirBnB platform, such as users, places, cities, and more.
2. **Web Static:** In this phase, you'll learn how to properly use HTML/CSS and create the static front-end of the AirBnB clone.
3. **MySQL storage:** This phase involves setting up a MySQL database to store objects created through the console.
4. **Web framework - templating:** In this phase, you'll create the server-side of the AirBnB clone using a web framework and integrate it with the storage engine.
5. **RESTful API:** The final phase involves creating a RESTful API that allows other software to interact with the AirBnB clone.

This repository covers the first phase of the project: the Console.

## Console

The console is a command-line interface that allows users to manage objects related to the AirBnB platform. It provides a set of commands to create, update, and manipulate objects such as users, places, cities, and more.
**Getting Started**

1. Clone the repository:
    git clone https://github.com/your_username/AirBnB_clone.git
2. Navigate to the project directory:
    cd AirBnB_clone
3. Run the console:
    ./console.py

**Usage**
Once the console is running, you can use the following commands:

- `help`: Displays a list of available commands.
- `quit`: Exits the console.
- `create <class>`: Creates a new instance of the specified class.
- `show <class> <id>`: Displays the string representation of an instance.
- `destroy <class> <id>`: Deletes an instance based on the class and ID.
- `update <class> <id> <attribute> <value>`: Updates an instance's attribute with the specified value.
- `all <class>`: Displays all instances of the specified class.

For more detailed information on the available commands and their usage, refer to the documentation within the console or type `help <command>` for command-specific help.
**Testing**
You can run the provided test suite to ensure the project's functionality. Make sure all tests pass in non-interactive mode by executing the following command:

    echo "python3 -m unittest discover tests" | bash
## Contributing

Contributions to this project are welcome. If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

