

#so classes a datetypes that we can make
# because not everything can be represented in
# strings, boolean values and numbers so than a computer can understand it


# lets say we want to model a student from school
# we can make a class for this because a stuednt is not a data type in py
class student:
    #every thing in this is in the student class
    # so we are makeing a student in here
    def __init__(self, name, major, gpa, is_on_probation ):
        #in the bracket we describe we describe the student
        # in here we describe a student to the computer
        # here we describe the objects
        # so when you store a name it is being stored in self.name then we convert it so then it is easyer for
        # you by just name
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation
