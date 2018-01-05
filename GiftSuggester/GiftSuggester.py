import os.path
import os 

import random

class Person(object):

    def __init__(self, name):
        self.name = name
        dir_path = os.path.dirname(os.path.realpath(__file__))
        self.address = dir_path + "/People/" + name + ".txt"
        self.ideas = []

        if os.path.exists(self.address):
            with open(self.address, "r") as file:
                data = file.readline()
                items = data.split(",")
                for item in items:
                    self.ideas.append(item)

        else:
            with open(self.address, "w+") as file:
                file.writelines("")

    def add_idea(self, idea):
        if idea == "":
            print("Invalid input")
            return
        for item in self.ideas:
            if item == idea:
                print("Sorry, that's already been added!")
                return

        self.ideas.append(idea)
        with open(self.address, "r") as file:
            data = file.readlines()

        with open(self.address, "w") as file:
            data.append(idea + ",")
            file.writelines(data)

    def get_idea(self):
        if len(self.ideas) > 0:
            index = random.randrange(0, len(self.ideas))
            print(self.ideas[index])
        else:
            print("Sorry, doesn't look like we have any data on " + self.name)

    def list_all(self):
        for idea in self.ideas:
            if idea != "":
                print('"' + idea + '"')

while True:
    print("Enter a person's name!")
    person = Person(input("> "))

    while True:
        print("Add, get random, or list")
        choice = input("> ")

        if "get" in choice:
            person.get_idea()
        
        elif "add" in choice:
            print("What idea is it?")
            person.add_idea(input("> "))

        elif "list" in choice:
            person.list_all()

        print("1: continue with same person, 2: continue with a different person, 0: quit")
        choice = input("> ").lower()
        if "0" in choice:
            raise SystemExit(0)
        if "2" in choice:
            break