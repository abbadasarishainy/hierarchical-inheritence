class person:
    def walk(self):
        print("Walking")
    def eating(self):
        print("Eating Cookies")
    def sleep(self):
        print("sleeping")
class student(person):
    def read(self):
        print("Reading")
    def write(self):
        print("writting")
class professional(person):
    def work(self):
        print("working")
    def login(self):
        print("Incoming")
    def salary(self):
        print("salary")
p=professional()
s=student()
p.walk()
p.work()
s.walk()
s.write()
