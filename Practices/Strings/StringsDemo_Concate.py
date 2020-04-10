#String concatination

greeting = "Hello"
name = "Samarth"

#message = greeting + ', ' + name +'. Welcome!'

#string formating
message_formate = '{}, {}. Welcome! '.format(greeting,name)
print(message_formate)


#f strings
message_f = f'{greeting}, {name}. Welcome!'
print(message_f)
