#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]


class Person:
    def __init__(self, name='Guido', job='Sales'):
        if job not in APPROVED_JOBS:
            print("Job must be in list of approved jobs.")
        else:
            self.name = name
            self.job = job

    def get_name(self):
        print("Retrieving name.")
        return self._name.title()

    def set_name(self, name):
        if type(name) == str and 0 < len(name) <= 25:
            print(f"Setting name to {name}.")
            self._name = name
        else:
            print("Name must be string between 1 and 25 characters.")

    name = property(get_name, set_name)
