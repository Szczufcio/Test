class Parent():

    def print_last_name(self):
        print("Szewczak")

class Child(Parent):
    def print_first_name(self):
        print('Olaf')

    def print_last_name(self):
        print('FuckFace')

ofal = Child()
ofal.print_first_name()
ofal.print_last_name()