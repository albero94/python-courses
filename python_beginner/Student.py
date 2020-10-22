class Student:

    def __init__(self, name:str, major:str, gpa:float, is_on_probation:bool) -> None:
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation

    def print_info(self) -> str:
        return f"{self.name}, {self.major}, {self.gpa}, {self.is_on_probation}"
