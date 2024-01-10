#!/usr/bin/python3
"""Module for the entry point for the command interpreter"""

import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """The instance for the cmd module superclass"""
    prompt = "(hbnb) "
    __classes = {
        "BaseModel"
    }

    def emptyline(self):
        """Shouldn’t execute anything upon an empty line
        """
        pass

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        return True

    # using aliasing to implement EOF
    do_EOF = do_quit

    def do_create(self, *args):
        """Creates a new instance of BaseModel and saves it to JSON
        and prints id
        """
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(args[0].id)
            storage.save()
            #print(arg.id)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
