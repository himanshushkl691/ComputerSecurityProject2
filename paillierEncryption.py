from phe import paillier
# Paillier encryption is only defined for non-negative integers less than publicKey.n


class customPaillier:
    def fastExpo(self, num, p):
        res = 1
        while p > 0:
            if p % 2 == 1:
                res = res*num
            p = p//2
            num = num*num
        return res

    def modN2Expo(self, num, p):
        m = self.N2
        res = 1
        while p > 0:
            if p % 2 == 1:
                res = (res*num) % m
            p = p//2
            num = (num*num) % m
        return res

    def mulModN2(self, a, b):
        return (a * b) % self.N2

    def addModN2(self, a, b):
        return (a + b) % self.N2

    def __init__(self):
        self.publicKey, self.privateKey = paillier.generate_paillier_keypair()
        self.g, self.n = (self.publicKey).g, (self.publicKey).n
        self.p, self.q = (self.privateKey).p, (self.privateKey).q
        self.phiN2 = self.p * self.q * (self.p - 1) * (self.q - 1)
        self.N2 = self.fastExpo(self.p, 2) * self.fastExpo(self.q, 2)

    def __repr__(self) -> str:
        return ('[g: ' + str(self.g) + ',n: ' + str(self.n) + ']')

    def encryptList(self, secretList):
        encryptedList = [(self.publicKey).encrypt(x).ciphertext()
                         for x in secretList]
        return encryptedList

    def decryptList(self, encryptedList):
        secretList = [(self.privateKey).raw_decrypt(x) for x in encryptedList]
        return secretList

    def computeCiphertextInverse(self, ciphertext):
        return self.modN2Expo(ciphertext, self.phiN2 - 1)
