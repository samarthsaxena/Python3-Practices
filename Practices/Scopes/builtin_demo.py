import builtins

print(dir(builtins))

for item in dir(builtins):
    print(item)


print(f'Total Number of items: {len(dir(builtins))}' )
