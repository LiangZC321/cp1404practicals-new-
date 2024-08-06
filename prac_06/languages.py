# from programming_language import ProgrammingLanguage
#
#
# def main():
#
#     python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
#     ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
#     visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
#
#     languages = [python, ruby, visual_basic]
#
#     for language in languages:
#         print(language)
#
#     print("The dynamically typed languages are:")
#     for language in languages:
#         if language.is_dynamic():
#             print(language.name)
#
# if __name__ == "__main__":
#     main()

from programming_language import ProgrammingLanguage

python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
print(python)

"""
The dynamically typed languages are:
Python
Ruby"""

languages = [python, ruby, visual_basic]

for language in languages:
    if language.is_dynamic():
        print(f'{language.name}')
