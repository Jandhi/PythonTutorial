def reverse(string : str) -> str:
    return string[::-1]

class Student:
    def __init__(self) -> None:
        self.name = 'Michael'
        self.year = 3

    def introduce(self) -> None:
        print(f'Hi I\'m {self.name}!')

michael = Student()