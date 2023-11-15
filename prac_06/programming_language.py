"""
Create a class for programming languages
"""


class ProgrammingLanguage:
    """class for computer language"""
    def __init__(self, name, typing, reflection, year):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """determine language typing type"""
        if self.typing == "Dynamic":
            return True

    def __str__(self):
        return (f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, "
                f"First appeared in {self.year}")

