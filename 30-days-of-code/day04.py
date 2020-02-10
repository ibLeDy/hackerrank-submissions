class Person():
    def __init__(self, initialAge):
        self.initialAge = initialAge
        self.age = age  # noqa

        if self.initialAge > 0:
            self.age = self.initialAge
        else:
            self.age = 0
            print("Age is not valid, setting age to 0.")

    def amIOld(self):
        if self.age < 13:
            print("You are young.")
        elif self.age >= 13 and self.age < 18:
            print("You are a teenager.")
        else:
            print("You are old.")

    def yearPasses(self):
        self.age += 1
