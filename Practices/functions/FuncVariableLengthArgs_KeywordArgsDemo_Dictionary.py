    #!/usr/bin/env python3

#To work with dictionary we need the key word based variable lenth kwargs
#

def main():
    kitten(Buffy='meow',Zilla='grr',Angel='rawr')

#To pass a dictionary we put ** in formal parameter
def kitten(**kwargs):
    if len(kwargs):
        for k in kwargs:
            print(f'Kitten {k} says {kwargs[k]}')
    else:
        print("All good :( ")

if __name__ == '__main__':
    main()
