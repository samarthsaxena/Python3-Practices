#!/usr/bin/python

import os


initialData = """version: 1

"""
dataDumpList=list()
usersDict=dict()
data=""
def createDataDump(initialUserNamePrefix, numberOfUsers, defaultPassword):
    """
    For creating a user records, which would be used for being written into a file
    returns
    """
    if initialUserNamePrefix is (None or ""):
        initialUserNamePrefix="testuser0"
    for i in range(1,numberOfUsers+1):
        stringnumber=str(i)
        testusernameTemp = initialUserNamePrefix + stringnumber
        print(testusernameTemp)

        #every user has these details
        data1=[f'dn: cn={testusernameTemp},o=novell\n',
		"""changetype: add\n""",
		f"""uid: {testusernameTemp}\n""",
		f"""givenName: Test User {stringnumber}\n""",
		f"""fullName: Test User {stringnumber}\n""",
		"""Language: ENGLISH\n""",
		"""sn: User\n""",
		f"""mail: {testusernameTemp}@microfocus.test\n""",
		"""telephoneNumber: 69333\n""",
		"""passwordAllowChange: TRUE\n""",
		"""objectClass: inetOrgPerson\n""",
		"""objectClass: organizationalPerson\n""",
		"""objectClass: Person\n""",
		"""objectClass: ndsLoginProperties\n""",
		"""objectClass: Top\n""",
		f"""cn: {testusernameTemp}\n""",
		f"""ACL: 2#subtree#cn={testusernameTemp},o=novell#[All Attributes Rights]\n""",
		f"""ACL: 6#entry#cn={testusernameTemp},o=novell#loginScript\n""",
		"""ACL: 2#entry#[Public]#messageServer\n""",
		"""ACL: 2#entry#[Root]#groupMembership\n""",
		f"""ACL: 6#entry#cn={testusernameTemp},o=novell#printJobConfiguration\n""",
		"""ACL: 2#entry#[Root]#networkAddress\n""",
		f"""userpassword: {defaultPassword}\n"""
        ]

        #Create a single record for every user from data1
        dataT = ''.join(data1)

        #An entry in the list for a user
        dataDumpList.append(dataT)

        #Create a Dictionary of users to avoid duplicates if any.
        usersDict.update({f'{testusernameTemp}':dataT})
        print(len(dataDumpList))
        print(usersDict)


def createLdifWithUsers(ldifFinalName):
    if os.path.exists(ldifFinalName):
        print(f'{ldifFinalName} already exists so removing and creating a new one for new user records.')
        os.remove(ldifFinalName)
    with open(ldifFinalName,'a+') as f:
        print(f"File created :{f.name}")

        f.write(initialData)
        lineCount = 1
        for dataCount in range(len(dataDumpList)):
            f.write(dataDumpList[dataCount])
            f.write('\n')
            lineCount += 1
            if lineCount == 24:
                f.write('\n')
                lineCount = 1


def readDataWrittenInFile(fileName):
    with open(fileName,'r') as file:
        line=file.readline()
        print('*\n'*10)
        #file.seek(os.path.getsize(file.))
        while line:
            line=file.readline()
            print(line)


def main():
    initUsername='testuser0'
    commonPassword='novell'
    usersFileName="nam-users.ldif"
    totalNumberOfUsers = 10

    print('Creating data dump')
    createDataDump(initUsername,totalNumberOfUsers,commonPassword)

    print(f"Appending {usersFileName} with user data dump")
    createLdifWithUsers(usersFileName)
    print('Operation Completed...')

    print(f'Total file size of {usersFileName} : {os.path.getsize(usersFileName)}')

    print()
    #Clear the console
    if os.name is 'posix' or 'POSIX':
        os.system('cls')
    elif os.name is 'nt' or 'NT':
        os.system('cls')

    #To print out the data
    readDataWrittenInFile(usersFileName)



if __name__ == '__main__':
    main()
