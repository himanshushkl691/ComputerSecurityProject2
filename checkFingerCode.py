from dist import *
from allPairDistComputation import *


def isPresent(rollNumber, fingercode, mydb, cryptSystem):
    encryptedFingerCode = cryptSystem.encryptList(fingercode)

    squaredSum = 0
    k = len(fingercode)
    for i in range(k):
        squaredSum = squaredSum + (fingercode[i] * fingercode[i])
    encryptedSquaredSum = cryptSystem.encryptList([squaredSum])[0]

    res = getAllEncryptedDist(
        encryptedSquaredSum, encryptedFingerCode, cryptSystem, mydb)
    # res = [[a1,b1],[a2,b2],....[an,bn]]    ai = encrypted roll, bi = encrypted distance
    T = 5  # Threshold
    for l in res:
        decryptDist = cryptSystem.decryptList([l[1]])[0]
        if decryptDist < T:
            decryptedRollNo = cryptSystem.decryptList([l[0]])[0]
            if rollNumber == decryptedRollNo:
                return True
    return False
