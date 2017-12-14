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

    def addIdea(self, idea):
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

    def getIdea(self):
        if len(self.ideas) > 0:
            index = random.randrange(0, len(self.ideas))
            print(self.ideas[index])
        else:
            print("Sorry, doesn't look like we have any data on " + self.name)

    def listAll(self):
        for idea in self.ideas:
            print('"' + idea + '"')

while True:
    print("Enter a person's name!")
    person = Person(input("> "))

    while True:
        print("Add, get random, or list")
        choice = input("> ")

        if "get" in choice:
            person.getIdea()
        
        elif "add" in choice:
            print("What idea is it?")
            person.addIdea(input("> "))

        elif "list" in choice:
            person.listAll()

        print("1: continue with same person, 2: continue with a different person, 0: quit")
        choice = input("> ").lower()
        if "0" in choice:
            raise SystemExit(0)
        if "2" in choice:
            break