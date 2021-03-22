class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.num = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.num >= self.step * self.count:
            raise StopIteration

        num = self.num
        self.num += self.step
        return num


numbers = take_skip(2, 6)
for number in numbers:
    print(number)


numbers = take_skip(10, 5)
for number in numbers:
    print(number)

