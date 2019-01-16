# CLASSES AND METHODS
class Person():
    def __init__(self, name, bio, age):
        # your code goes here!
        self.name = name
        self.bio = bio
        self.age = age

    def __str__(self):
        return "%s %s %s" % (self.name, self.age, self.bio)


class Club():
    def __init__(self, name, description):
        # your code goes here!
        self.name = name
        self.description = description
        self.members = []
        self.president = {}


    def assign_president(self, person):
        # your code goes here!
        self.president = person



    def recruit_member(self, person):
        # your code goes here!
        self.members.append(person)


    def print_member_list(self):
        # your code goes here!
        for member in self.members:
            print(member)
        print(str(self.president) + " (PRESIDENT OF THE CLUB)" )   


    def __str__(self):
        return "Name: %s \nDescription: %s \nMembers: %s" %(self.name , self.description, len(self.members))

