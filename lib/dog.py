#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]


class Dog:
    def __init__(self, name="Fido", breed=None):
        if breed and breed not in APPROVED_BREEDS:
            print("Breed must be in list of approved breeds.")
        else:
            self.name = name
            self.breed = breed

    def get_name(self):
        print("Retrieving name.")
        return self._name

    def set_name(self, name):
        if (type(name) == str and 0 < len(name) <= 25):
            print(f"Setting name to { name }.")
            self._name = name

        else:
            print("Name must be string between 1 and 25 characters.")

    name = property(get_name, set_name)


fido = Dog()
