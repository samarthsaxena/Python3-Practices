#!/usr/bin/env python3

def main():
    f = open('test.txt','r')
    for i in f:
        print(i.rstrip())

    f.close()

if __name__ == '__main__': main()
