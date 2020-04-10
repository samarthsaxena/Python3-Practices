user = 'admin'
logged_in = True

if user == 'admin' and logged_in:
    print('Admin Logged in')
else:
    print('Not logged in')

if user == 'Admin' or logged_in:

    print('Admin Logged in')

else:
    print('Not logged in')

if not logged_in:
    print("Please login ")
else:
    print("Already logged in")
