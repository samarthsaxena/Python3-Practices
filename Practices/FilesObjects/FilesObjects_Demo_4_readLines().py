#!/usr/bin/env python3
f_contents_lines = list()
with open('test.txt','r') as f:
    #Use readLines() which would return a list of lines
    f_contents_lines = f.readlines()


if f_contents_lines and f.closed:
    for content in f_contents_lines:
        print(content)
    print(f_contents_lines)
    print(len(f_contents_lines))
elif not f.closed:
    print("File is not closed")
elif not f_contents_lines:
    print("File content is None: ",f_contents_lines)
else:
    print('Sometihng is wrong !!')
