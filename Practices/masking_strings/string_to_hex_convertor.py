import os

"""
Python utility for sting to hex conversion
"""


class ToHex:

    def __init__(self):
        is_completed = False

    def convert_to_hex(self, input_string):
        input_string_len = len(input_string)
        print(f'the input string is \'{input_string}\' with length \'{input_string_len}\'')
        hex_list = [hex(ord(hex_value)) for hex_value in input_string]
        print(f'List of hex equivalents : {hex_list}')
        return hex_list


def withoutProperFormat():
    input_string = input("Input a string to convert into hex codes: ")
    result_list = ToHex().convert_to_hex(input_string.strip())
    full_conversion = ""
    for i in result_list:
        full_conversion += i
    print(full_conversion)
    print(f'After conversion length : {len(full_conversion)}')


if __name__ == '__main__':
    withoutProperFormat()
    print(f'This is end of the __main__')
