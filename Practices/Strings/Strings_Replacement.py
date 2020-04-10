#Replace strings


about_replace = """#replace returns a new string but does not change the original string
#So here we must receive the new string returnd by replace method and set this to original
#variable """

message = "Hello World"

message.replace('World','Universe')

print(message)
print("--------------------")
print(about_replace)
print("--------------------")


message = message.replace("World",":)")
print(message)
