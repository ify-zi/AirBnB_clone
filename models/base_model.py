#!/usr/bin/python3

"""Define the base model class"""

import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Represents the BaseModel of our project and the parent class"""

    def __init__(self, *args, **kwargs):
        """Initializes a new object/instance
        Args:
            *args(any): Unused
            **kawargs(dict): key&value pairs of attributes
        """
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for i, j in kwargs.items():
                if i == "created_at" or i == "updated_at":
                    self.__dict__[i] = datetime.strptime(j, tform)
                else:
                    self.__dict__[i] = j
        else:
            models.storage.new(self)

    def to_dict(self):
        """Return the dictionary of the BaseModel instance.
        Includes the key/value pair __class__ which represents
        the class name of the object.
        """
        rdict = self.__dict__.copy()
        rdict["created_at"] = self.created_at.isoformat()
        rdict["updated_at"] = self.updated_at.isoformat()
        rdict["__class__"] = self.__class__.__name__
        return rdict

    def save(self):
        """Update updated_at with the current datetime."""
        self.updated_at = datetime.today()
        models.storage.save()

    def __str__(self):
        """Return the print/str representation of the BaseModel instance."""
        clname = self.__class__.__name__
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)
