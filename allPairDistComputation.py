from dist import *


def getAllEncryptedDist(encryptedSquaredSum, encryptedFingercode, cryptSystem, mydb):
    queryResult = mydb.fingercode.find()
    res = []
    for q in queryResult:
        encryptedRollNo = int(q['Data1'])
        fingercode = q['Data2']
        encryptedDistance = squaredEuclideanDistance(
            cryptSystem, encryptedFingercode, encryptedSquaredSum, fingercode)
        res.append([encryptedRollNo, encryptedDistance])
    return res
