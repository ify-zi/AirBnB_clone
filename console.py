#!/usr/bin/env python3
"""
    AirBnB-clone Console Module
"""


import cmd


class HBNBCommand(cmd.Cmd):
    """
        CLI console of AirBnB clone project
    """


    prompt = '(hbnb) '

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
    HBNBCommand().cmdloop()
