# with Iterator

class vowels:
    vowels = {'a', 'e', 'y', 'u', 'o', 'i',
              'A', 'E', 'Y', 'U', 'O', 'I'}

    def __init__(self, text):
        self.text = text
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.text):
            raise StopIteration

        char = self.text[self.index]
        self.index += 1

        if char not in self.vowels:
            return self.__next__()

        return char

# with Generator function

# def vowels(text):
#     vowels = {'a', 'e', 'y', 'u', 'o', 'i',
#               'A', 'E', 'Y', 'U', 'O', 'I'}
#
#     for char in text:
#         if char in vowels:
#             yield char

# with generator comprehension

# def vowels(text):
#     vowels = {'a', 'e', 'y', 'u', 'o', 'i',
#               'A', 'E', 'Y', 'U', 'O', 'I'}
#
#     return (ch for ch in text if ch in vowels)

my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)






