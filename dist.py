def squaredEuclideanDistance(paillierCryptSys, X, X_squaredSum, Y):
    res1 = 1
    res2 = 0
    k = len(X)
    for i in range(0, k):
        X_i_inv = paillierCryptSys.computeCiphertextInverse(X[i])
        res1 = paillierCryptSys.mulModN2(
            res1, paillierCryptSys.modN2Expo(X_i_inv, 2*Y[i]))
        res2 = paillierCryptSys.addModN2(res2, (Y[i]*Y[i]))

    res2 = paillierCryptSys.encryptList([res2])[0]

    res = paillierCryptSys.mulModN2(X_squaredSum, res1)
    res = paillierCryptSys.mulModN2(res, res2)
    # encrypted distance
    return res
