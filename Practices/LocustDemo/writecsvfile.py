import os
import csv

dataDumpList = list()
csv_filename = 'testusers-dump.csv'


def createDataDump(initialUserNamePrefix, numberOfUsers, defaultPassword):
    """
    For creating a user records, which would be used for being written into a file
    returns
    """

    dataDumpList.append(["user", "password"])
    if initialUserNamePrefix is (None or ""):
        initialUserNamePrefix = "testuser0"
    for i in range(1, numberOfUsers + 1):
        stringnumber = '{num:0{width}}'.format(num=i, width=2)
        testusernameTemp = initialUserNamePrefix + stringnumber

        dataDumpList.append([testusernameTemp, defaultPassword])

    if os.path.exists(csv_filename):
        os.remove(csv_filename)
    with open(csv_filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(dataDumpList)


def main():
    createDataDump("testuser", 1000, "novell")
    print("Done")


if __name__ == '__main__':
    main()
