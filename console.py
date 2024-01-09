#!/usr/bin/python3
"""Module for the entry point for the command interpreter"""

import cmd


class HBNBCommand(cmd.Cmd):
    """The instance for the cmd module superclass"""
    prompt = "(hbnb) "

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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
