class Person:
    def __init__(self,name,age,address):
        self._name = name
        self._age = age
        self._address = address

    def get_name(self):
        return self._name

    def set_name(self,name):
        self._name = name

    def get_age(self):
        return self._age

    def set_age(self,age):
        self._age = age

    def get_address(self):
        return self._address

    def set_address(self, address):
        self._address = address

