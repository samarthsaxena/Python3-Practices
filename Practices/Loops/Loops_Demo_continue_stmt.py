nums = [1,2,3,4,5]

for num in nums:
    print("In side loop")
    if num == 3:
        print('Found')
        continue
        print('After continue')
    print(num)
