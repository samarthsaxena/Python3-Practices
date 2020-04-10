#!/usr/bin/env python3

def main():
    """
    Function to copy a jpg image and create a new one
    """
    infile = open('samarth.jpg','rb') # read in binary mode
    outfile = open('samarth-copy.jpg','wb') #write in binary mode

    while True:
        buffer = infile.read(1024) #Reading 1 KB at a time
        if buffer:
            outfile.write(buffer)
            print('.', end='', flush=True)
        else:
            break
    outfile.close()
    infile.close()

    print('\nDone')

if __name__ =='__main__':
    main()
