#!/usr/bin/env python3

import sys
import os
import hashlib as hl


"""
Demo for hashlib module
Checking the md5 / SHA1 / SHA224 / SHA256 / SHA384 / SHA512 hashes.

"""

#Optional Method
def come_to_root():
    os.chdir('/')
    return

def list_files():
    return os.system('find / -iname *.py')

# def calculate_checksum(with_algorithm):
#     """
#     Returns list of algos for checksum calculations(Objects of algos)
#     """

#     list_supported_algos = list('md5','sha1','sha256','sha512')
#     objects_of_algos = list()

#     if len(with_algorithm) == 1 and with_algorithm in list_supported_algos:
#         if with_algorithm[0] =='md5':
#             return hl.md5()
#         elif with_algorithm[0] =='sha1':
#             return hl.sha1()
#         elif with_algorithm[0] =='sha256':
#             return hl.sha256()
#         elif with_algorithm[0] =='sha512':
#             return hl.sha512()
#     elif len(with_algorithm) > 1:
#         for needed_algos in with_algorithm:
#             objects_of_algos



def hello():
    come_to_root()
    list_files()


if __name__ == '_main_':
    hello()
        

