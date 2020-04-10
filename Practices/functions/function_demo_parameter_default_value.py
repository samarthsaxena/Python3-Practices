def happy_function(greeting, name = 'Samarth'):
	return f'{greeting}, {name} :)'

def good_morning_function(greeting = 'Good Morning',name ="samarth"):
	return f'{greeting}..... {name}'


print(happy_function('Good Day','Poornima'))
print(happy_function('Hello'))
print(happy_function('Night night',''))

print('-------------------------------------------')

	
print(good_morning_function(name='Poornima'))
print(good_morning_function('','Hello'))
print(good_morning_function('Night night'))