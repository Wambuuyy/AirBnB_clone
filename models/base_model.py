#!/usr/bin/python3
"""
defines all common attributes and methods for other classes:
    1. public attributes:
        id: assign with uuid when instance is
        created to always have a unique id
        created _at: assign using datetime
        updated_at: assign using datetime
    2. __str__: should prnt clsnam id dict
    3. public methods:
        save: updates the updated_at with datetime
        to_dict: returns a dictionary containing all keys/values
        of __dict__ of the instance:
            use self.__dict__ only attributes are returned
            key __class__ must be added to the dict
            with classneme of the object
            created_at and updated_at must be
            converted to a string in ISO format:
            the method will be the first piece of serialization
"""

from datetime import datetime
import uuid
from models import storage


class BaseModel:
    def __init__(self, *args, **kwargs):
        """
        BaseModel constructor
        """
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

        # check if kwargs is not None and not empty
        if kwargs is not None and kwargs != {}:
            # iterate through key-value pairs in kwargs
            for key, value in kwargs.items():
                # skip setting __class__ attribute
                if key == "__class__":
                    continue
                # Convert created_at and updated_at strings to datetime objects
                elif key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(value, time_format))
                else:
                    # set other attributes
                    setattr(self, key, value)
        storage.new(self)

    def __str__(self):
        """
        """
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        """
        """
        self.updated_at = datetime.utcnow()
        storage.save()

    def to_dict(self):
        """
        """
        # to avoid modifying the original dict directly
        my_dict = self.__dict__.copy()
        # Add the '__class__' key with the class name to the dictionary
        my_dict["__class__"] = self.__class__.__name__
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()

        return my_dict
