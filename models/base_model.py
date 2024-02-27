#!/usr/bin/python3

"""Class BaseModel defines all common attributes/methods for other classes"""


from uuid import uuid4
import datetime


class BaseModel:
    """class Basemodel"""

    def __init__(self, *args, **kwargs):
        self.id = str(uuid4())
        if kwargs is not None:
            for key, value in kwargs.items():
                if key != "__class__":
                    attribute_name = key
                    attribute_value = value
                    if attribute_name in ["created_at", "updated_at"]:
                        self.created_at = datetime.datetime.strptime(
                            attribute_value, '%Y-%m-%dT%H:%M:%S.%f')
                        self.updated_at = datetime.datetime.strptime(
                            attribute_value, '%Y-%m-%dT%H:%M:%S.%f')
                    else:
                        setattr(self, attribute_name, attribute_value)
        else:
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        dict_copy = self.__dict__.copy()
        dict_copy['__class__'] = self.__class__.__name__
        dict_copy['created_at'] = self.created_at.isoformat()
        dict_copy['updated_at'] = self.updated_at.isoformat()
        return dict_copy


my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89
print(my_model.id)
print(my_model)
print(type(my_model.created_at))
print("--")
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

print("--")
my_new_model = BaseModel(**my_model_json)
print(my_new_model.id)
print(my_new_model)
print(type(my_new_model.created_at))

print("--")
print(my_model is my_new_model)