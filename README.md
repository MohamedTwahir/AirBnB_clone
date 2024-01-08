# 0x00. AirBnB clone - The console
The project is a clone of the AirBnB website.
We wont be implementing all the features at a go instead some features step by step and by end of the four months we will have deployed a ready website that is a clone of the AirBnB with we will call it hbnb.
# Steps
I wont be building the application all at once:
* The console(The command interpreter)
1. creating my data model
2. managing objects via a console
3. storing and persisting objects to a file (JSON file)

The first piece is to manipulate a powerful storage system. This storage engine will give us an abstraction between “My object” and “How they are stored and persisted”. This means: from your console code (the command interpreter itself) and from the front-end and RestAPI you will build later, you won’t have to pay attention (take care) of how your objects are stored.

This abstraction will also allow you to change the type of storage easily without updating all of your codebase.

The console will be a tool to validate this storage engine.

# Description of the command interpreter
The console is just like a shell but with a specific use.
Which is to manage objects of our projects:
1. Create a new object
2. Retrieve an object from a file, a database 
3. Do operations on objects
4. Update attributes of an object
5. Destroy an object
# How to start it
The console will be created with the help of the cmd module.
The module is available in python standard library

1. You first start by creating a file called console in your terminal:
~ touch console.py
2. open the file using a text editor of your choice. For me i will be using vi
~ vi console.py
3. Start by importing the cmd module in your file:
~ import cmd
4. The cmd module is useful as a superclass of an interpreter class you define for yourself. In my example i created a subclass HBNBCommand which inherits from the cmd module as the super class. So from now my code should look like this:
~ import cmd
~ class HBNBCommand(cmd.Cmd):
	"""My entry point for the command interpreter"""
	pass
5. But as of now you would want to  customize your prompt.
The cmd module has a public instance variable named prompt which allows you to customize your prompt. So your code should now look like this:
~ import cmd
~ class HBNBCommand(cmd.Cmd):
	"""My Entry point for the command interpreter"""
	prompt = '(hbnb) '

6. As from now you can notice the program is not in a continous loop. For that you will need cmdloop() object.
~ import cmd
~ class HBNBCommand(cmd.Cmd):
	"""My Entry point for the command interpreter"""
	prompt = '(hbnb) '
if __name__ == '__main__':
	HBNBCommand().cmdloop()
7. So right now you have a console with no command just interactive one.
# How to start your console
you just write the following code in the directory where your console.py exists
~ python3 console.py

Your shell should work like this in interactive mode:
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
help

(hbnb) 
(hbnb) 
(hbnb) quit
$

