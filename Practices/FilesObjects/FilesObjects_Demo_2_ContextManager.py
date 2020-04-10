#!/usr/bin/env python3

#everytime you open a file , you open a connection and your application may run if __name__ == '__main__':
    #memory leaks if file is forgotten to be closed
    #ContextManager helps to do this automatically for us
    #The file object variable exists within the with context manager and outside of it this object is vanised
    #so f.close() is purely optional
with open('test.txt', 'r') as f:
    print(f.name)
    #if it's a larg file then directly reading the file is not a good thing
    f_contents = f.read()
    print(f_contents)

    #This readLine() would return line by line results
    f_contents_line = f.readline()
    print(f_contents_line)


print(f.closed)
