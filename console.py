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

class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand console class
    """
    prompt = "(hbnb) "
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

if __name__ == "__main__":
    HBNBCommand().cmdloop()
