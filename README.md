AirBnB clone - The console

Description:

This team project is part of the ALX School Full-Stack Software Engineer program. It's the first step towards building a first full web application: an AirBnB clone. This first step consists of a custom command-line interface for data management, and the base classes for the storage of this data. Console commands allow the user to create, update, and destroy objects, as well as manage file storage. Using a system of JSON serialization/deserialization, storage is persistent between sessions.

Usage:

Command					Example
*run the console			./console.py

*quit the console			(hbnb) quit

*display the help for a command		(hbnb) help <command>

*create an object(prints its id)	(hbnb) create <class>

*show an object				(hbnb) show <class> <id> or (hbnb) <class>.show(<id>)

*destroy an object			(hbnb) destroy <class> <id> or (hbnb) <class>.destroy(<id>)

*show all objects
or all instances of a class		(hbnb) all or (hbnb) all <class>

*update an attribute of an object	(hbnb) update <class> <id> <attribute name> "<attribute value>"
						or
					(hbnb) <class>.update(<id>, <attribute name>, "<attribute value>") 
