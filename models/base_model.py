#!/usr/bin/python3
'''
Module for base model
'''


import models
import uuid
from datetime import datetime


class BaseModel:
    '''
    Class for base objects
    '''

    def __init__(self, *args, **kwargs):
        """
        Initalization of attributes
        """
        from models import storage
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ["created_at", "updated_at"]:
                        setattr(
                            self,
                            key,
                            datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        '''
        String representation of the instance
        '''
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        '''
        updates updated_at with the current datetime
        '''
        from models import storage

        self.updated_at = datetime.now()
        storage.save()
        return self.updated_at

    def to_dict(self):
        '''
        returns a dictionary with all
        keys/values of __dict__ of the instance
        '''
        data = self.__dict__.copy()
        data['__class__'] = self.__class__.__name__
        data['created_at'] = self.created_at.isoformat()
        data['updated_at'] = self.updated_at.isoformat()
        return data
