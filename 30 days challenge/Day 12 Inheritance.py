print_object = print


def print(*items_to_print):
    if 'Grade: ' in items_to_print:
        items_to_print = map(str, items_to_print)

        print_object(''.join(items_to_print))
    else:
        print_object(*items_to_print)


class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)


class Student(Person):
    #   Class Constructor
    def __init__(self, firstName, lastName, idNumber, scores):
        Person.__init__(self, firstName, lastName, idNumber)
        self.scores = scores
    #
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here

    def calculate(self):
        avg = sum(self.scores)/len(self.scores)
        if avg >= 90 and avg <= 100:
            letter = 'O'
        elif avg >= 80 and avg < 90:
            letter = 'E'
        elif avg >= 70 and avg < 80:
            letter = 'A'
        elif avg >= 55 and avg < 70:
            letter = 'P'
        elif avg >= 40 and avg < 55:
            letter = 'D'
        else:
            letter = 'T'
        return letter

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here


line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input())  # not needed for Python
scores = list(map(int, input().split()))
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
