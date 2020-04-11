from string import Template


def main():
    #Usual string formating with format()
    str1 = "You're having fun with {0} here Mr. {1} ;)".format("Adv Python", "Samarth Saxena")
    print(str1)


#Create a template with placeholders
    templ = Template("You're having fun with ${title} here Mr. ${name} ")
#Use Substitute method with keyword arguement
    str2 = templ.substitute(title="Advanced Python",name='Samarth')
    print(str2)

#use a substitute method with dictionary
    data = {
        'title' : 'Advanced PY',
        'name' : 'Samarth:)'
    }
    str3 = templ.substitute(data)
    print(str3)

if __name__ == '__main__':
    main()