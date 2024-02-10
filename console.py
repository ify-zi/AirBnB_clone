#!/usr/bin/python3
"""
    AirBnB-clone Console Module
"""


import cmd
from models.base_model import BaseModel
from models import storage
import sys


classes = {"BaseModel" : BaseModel}


class HBNBCommand(cmd.Cmd):
    """
        CLI console of AirBnB clone project
    """
    

    prompt = '(hbnb) '

    def do_create(self, class_name):
        """
            create an instance of BaseModel class
        """
        if class_name:
            if class_name in classes:
                new_class = classes[class_name]()
                new_class.save()
                print(new_class.id)
            else:
                print("** class doesn't exit **")
        else:
            print("** class is missing **")

    def do_show(self, class_params):
        """
            returns a string representatio of instance
        """
        if len(class_params) == 0:
            print("** class name missing **")
            return
        args = class_params.split()
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        try:
            if args[1]:
                name = "{}.{}".format(args[0], args[1])
                if name not in storage.all().keys():
                    print("** no instance found **")
                else:
                    print(storage.all()[name])
        except IndexError:
            print("** instance id missing **")

    def do_destroy(self, class_params):
        """
            Deletes an Instance of a class
        """
        if len(class_params) == 0:
            print("** class name missing **")
            return
        #split the string input a list "args"
        args = class_params.split()
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        if args[1]:
            name = "{}.{}".format(args[0], args[1])
            if name not in storage.all().keys():
                print("** no instance found **")
            else:
                del storage.all()[name]
                storage.save()

    def do_quit(self, line):
        """
            Quit command to exit program
        """
        return True

    def do_EOF(self, line):
        """
            Handles interupts 'EOF'
	"""
        return True

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        HBNBCommand().onecmd(' '.join(sys.argv[1:]))
    else:
        HBNBCommand().cmdloop()
