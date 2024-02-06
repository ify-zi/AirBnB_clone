#!/usr/bin/env python3
"""
    Base Model Module
"""


from datetime import datetime
import uuid

time = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """
        Base Model class instance
    """

    def __init__(self, *args, **kwargs):
        """
            initialization constructor of base class
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            if hasattr(self, "created_at") and type(self.created_at) is str:
                self.created_at = datetime.strptime(kwargs["created_at"], time)
            if hasattr(self, "updated_at") and type(self.updated_at) is str:
                self.updated_at = datetime.strptime(kwargs["updated_at"], time)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def __str__(self):
        """
            prints a formatted string to stdout
        """
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id,
                                         self.__dict__)

    def save(self):
        """
            updates time at @update_at with current time
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
            returns dict of self.__dict__ with class in it
        """
        class_dict = self.__dict__.copy()
        if "created_at" in class_dict:
            class_dict["created_at"] = class_dict["created_at"].strftime(time)
        if "updated_at" in class_dict:
            class_dict["updated_at"] = class_dict["updated_at"].strftime(time)
        class_dict["__class__"] = self.__class__.__name__
        
        return class_dict
