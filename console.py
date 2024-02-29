#!/usr/bin/env python3
"""
This module contains the entry point of the command interpreter.
"""

import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class definition
    """

    prompt = '(hbnb) '

    def do_quit(self, arg):
        """
        Quit command to exit the program
        """
        exit(0)

    def do_EOF(self, arg):
        """
        EOF command to exit the program
        """
        print()
        exit(0)

    def emptyline(self):
        """
        An empty line + ENTER shouldn’t execute anything
        """
        pass

    def do_create(self, line):
        """Create a new instance, save it, and print its ID."""
        if not line:
            print("** class name missing **")
            return

        args = line.split()
        if args[0] not in self.valid_classes:
            print("** class doesn't exist **")
            return
        new_instance = eval(args[0])()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, line):
        """Print the string representation of an instance
        based on class name and ID."""
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in self.valid_classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        obj_id = args[1]
        key = "{}.{}".format(args[0], obj_id)
        obj_dict = BaseModel.storage.all()
        if key in obj_dict:
            obj = obj_dict[key]
            print(obj)
        else:
            print("** no instance found **")

if __name__ == '__main__':
    interpreter = HBNBCommand()
    interpreter.cmdloop()
