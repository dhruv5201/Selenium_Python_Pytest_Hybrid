class student:
    studentName = ''

    def __init__(self, name):
        self.studentName = name

    def getName(self):
        return self.studentName


student1 = student('Dhrubajit')
print(student1.getName())
