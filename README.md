# AirBnB Console - Holberton School

## Description of the Project

This project is the first step towards building our first full web application: the AirBnB clone. This console will help us manage our AirBnB objects. It's a command interpreter that's designed to manage the objects of our AirBnB clone and perform functions like creating new objects, retrieving an object from a file, doing operations on them, and updating the attributes of an object.

## Description of the Command Interpreter

The command interpreter is designed to manage the objects of our AirBnB clone. It's a console that you can run in your terminal to execute commands and manage your objects.

### How to Start It

You can start the console by running `console.py`:

```bash
./console.py
```

This will start the console and wait for you to enter a command.

### How to Use It
The console supports the following commands:
```
show: Shows an instance based on the class name and id. For example, show BaseModel 1234-1234-1234 will show the BaseModel instance with the id 1234-1234-1234.
create: Creates a new instance of a class. For example, create User will create a new User instance.
destroy: Destroys an instance based on the class name and id. For example, destroy User 1234-1234-1234 will destroy the User instance with the id 1234-1234-1234.
update: Updates an instance based on the class name and id. For example, update User 1234-1234-1234 email "aibnb@holbertonschool.com" will update the email attribute of the User instance with the id 1234-1234-1234.
all: Shows all instances of a class, or all instances of all classes if no class is specified. For example, all User will show all User instances, and all will show all instances of all classes.
```

### Examples

Here are some examples of how to use the console:

```
./console.py
(hbnb) create User
(hbnb) show User 1234-1234-1234
(hbnb) destroy User 1234-1234-1234
(hbnb) update User 1234-1234-1234 email "aibnb@holbertonschool.com"
(hbnb) all
```

### Project Tasks
```
1. Write a command interpreter to manage your AirBnB objects. This is the first step towards building your first full web application: the AirBnB clone.
2. Put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances.
3. Create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file.
4. Create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel.
5. Create the first abstracted storage engine of the project: File storage.
6. Create all unittests to validate all our classes and storage engine.
```

### Future Work
This project is the first step towards building a full web application. The next steps will involve creating HTML/CSS templates, setting up database storage, creating an API, and integrating the front-end.


### AUTHORS

- [@arbesavdiaj](https://github.com/arbesavdiaj)
- [@FloriMecaj](https://github.com/FloriMecaj)
- [@Remz97](https://github.com/Remz97)
