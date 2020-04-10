#!/usr/bin/env python3

def main():
    """
    Function to copy a text file contents and create a new one
    """
    infile = open('test.txt','rt')
    outfile = open('test-copy.txt','wt')
    for line in infile:
        print(line.rstrip(),file=outfile)
        print('.' , end='', flush=True)

    outfile.close()
    infile.close()
    print('\nDone')

if __name__ == '__main__':
    main()
