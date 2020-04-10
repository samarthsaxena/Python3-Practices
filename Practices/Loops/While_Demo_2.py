# with break, continue, pass key words

print("Break keywork")

x = 0

while x < 10:
    if x == 5:
        break
        print(x)
    print(x)
    x += 1

print()
print("Pass keywork")
x = 0

while x < 10:
    if x == 5:
        pass
        print(x)
    print(x)
    x += 1
print()

print("Continue keywork")


x = 0

while x < 10:
    if x == 5:
        continue
        #print(x)
    #print(x)
    x += 1

print(x)

print("End----")
