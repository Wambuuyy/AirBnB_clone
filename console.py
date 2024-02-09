#!/usr/bin/python3
"""
contains the entry point of the command interpreter
uses cmd module
implements quit and EOF to exit the program
implements help although its defaulted we keep it updated
custom prompt (hbnb)
implements empty line and enter does nothing
it's not executed when imported but when called
"""
import cmd
import json
import models
from models.base_model import BaseModel
import shlex # we are parsing command-line input that includes quoted strings

class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand console class
    """
    prompt = "(hbnb) "
    valid_classes = {
            "BaseModel": BaseModel,
            # Add more class mappings as needed
            }


    def do_quit(self, arg):
        """
        implements quit to exit the program
        """
        return True

    def emptyline(self):
        """
        do nothing on emptyline and enter
        """
        pass

    def do_EOF(self, arg):
        """
        implement EOF to exit the program
        """
        print()
        return True

    def help_quit(self):
        """Help message for the quit command"""
        print("Quit command to exit the program")
        print()

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, saves it (to the JSON file)
        prints the id. Ex: $ create BaseModel
        """
        commands = shlex.split(arg)
        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
        else:
            class_name = commands[0]
            class_obj = self.valid_classes[class_name] # get the class object from the dictionary
            new_instance = class_obj() # instantiate a new object of the specified class
            storage.save() # save the new instance to the JSON file
            print(new_instance.id)

if __name__ == "__main__":
    HBNBCommand().cmdloop()
