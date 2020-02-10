class Student(Person):  # noqa
    def __init__(self, firstName, lastName, idNumber, scores):
        super().__init__(firstName, lastName, idNumber)
        self.scores = scores

    def calculate(self):
        result = sum(self.scores) // len(self.scores)
        return 'O' if result > 89 else 'E' if result > 79 else 'A' if result > 69 else 'P' if result > 54 else 'D' if result > 39 else 'T'
