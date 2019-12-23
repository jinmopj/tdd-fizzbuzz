class fizzbuzz():
    def convert(self):
        if self % 3 == 0:
            return 'Fizz'
        if self % 5 == 0:
            return 'Buzz'
        return str(self)
