from pymongo import MongoClient
from pprint import pprint
from datetime import datetime

from attendanceDB import *
from checkFingerCode import *
from paillierEncryption import *

client = MongoClient("mongodb://localhost:27017/")
mydb = client.AttendanceSystem

cryptSystem = customPaillier()

while True:
    print('1. Register yourself\n')
    print('2. Mark your attendance\n')
    print('3. Exit\n')
    optionPicked = int(input('Your option: '))

    if optionPicked == 1:
        rollNumber = int(input("Enter the Roll Number: "))
        query = {'registeredRollNumber': str(rollNumber)}
        queryResult = mydb.registeredStudent.count_documents(query)
        if(queryResult == 1):
            print('Already registered\n')
        else:
            print('Enter your fingercode: ', end='')
            fingercode = [int(x) for x in input().split()]
            data1 = str(cryptSystem.encryptList([rollNumber])[0])
            query = {'Data1': data1, 'Data2': fingercode}
            resultQuery = mydb.fingercode.insert_one(query)
            if resultQuery.inserted_id:
                query = {'registeredRollNumber': str(rollNumber)}
                mydb.registeredStudent.insert_one(query)
                print('Successfully registered\n')
            else:
                print('Try again\n')
    elif optionPicked == 2:
        rollNumber = int(input("Enter the Roll Number: "))
        print('Enter your fingercode: ', end='')
        fingercode = [int(x) for x in input().split()]
        timestamp = datetime.now()
        queryResult = isPresent(rollNumber, fingercode, mydb, cryptSystem)
        if(queryResult == True):
            markingResult = markAttendance(str(rollNumber), timestamp, mydb)
            if(markingResult == True):
                print("Successfully marked\n")
            else:
                print(
                    "Error in marking attendance although the credentials matched,try again\n")

        else:
            print("No match found, maybe you are not registered\n")
    else:
        break
