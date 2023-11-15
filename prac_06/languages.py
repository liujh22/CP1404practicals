"""
Clint code to use programming_language.py
"""

from prac_06.programming_language import ProgrammingLanguage


def main():
    """three languages using class example"""
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    print(python)
    mylist = [python, ruby, visual_basic]
    print_dynamic_type(mylist)


def print_dynamic_type(mylist):
    """print if languages in the list is dynamic"""
    print("The dynamically typed languages are:")
    for language in mylist:
        if language.is_dynamic():
            print(language.name)


main()
