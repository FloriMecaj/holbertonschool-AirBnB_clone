#!/usr/bin/python3
"""Defines the HBnB console."""
import cmd

class HBNBCommand(cmd.Cmd):
    """Defines the HolbertonBnB command interpreter"""

    prompt = "(hbnb) "

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass



    def do_quit(self, arg):
        """Quit command to exit the program."""
        exit(0)

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        print()
        exit(0)

if __name__ == "__main__":
    HBNBCommand().cmdloop()
