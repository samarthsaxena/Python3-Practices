"""
strings and bytes are not directly interchangable.
strings contiain unicode, bytes are unicode 8-bit raw values.
"""

def main():
    s = "This is a string."
    print(s)

    b = bytes([0x41,0x42,0x43])
    print(b)
#O/P:
#This is a string.
#b'ABC'
#Que: How to prove this? Well, we can try contactination of string s and bytes b and let's see what happens
    #print(s+b)
#O/P: TypeError: can only concatenate str (not "bytes") to str
# In-order to do that we need to decode the uni code to asci
    s2 = b.decode('utf-8') # utf-8 is already known here so we picked it, otherwise some custome logic must have been implemented.
    print(s+s2) #This is a string.ABC

    #string to bytes encoding 
    b2 = s.encode('utf-8')
    print(b+b2)

if __name__ == '__main__':
    main()


