#!/usr/bin/python3
"""Module for the entry point for the command interpreter"""

import cmd
from models.base_model import BaseModel
from models import storage


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
            new_instance = HBNBCommand.__classes[args[0]]()
            print(new_instance.id)
            storage.save()

    def do_show(self, *args):
        """ Prints the string representation of
        an instance based on the class name and id
        """
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            all_objects = storage.all()
            if key not in all_objects:
                print("** no instance found **")
            else:
                print(all_objects[key])

    def do_destroy(self, *args):
        """Deletes an instance based on
        the class name and id (save the change into the JSON file)
        """
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            all_objects = storage.all()
            if key not in all_objects:
                print("** no instance found **")
            else:
                del all_objects[key]
                storage.save()

    def do_all(self, *args):
        """Prints all string representations of
        instances based or not on the class name."""
        all_objects = storage.all()
        if len(args) == 0:
            print([str(obj) for obj in all_objects.values()])
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print([str(obj) for key, obj in all_objects.items() if key.split('.')[0] == args[0]])


if __name__ == '__main__':
    HBNBCommand().cmdloop()