from tinyec import registry
import secrets
import time
#For Display Purpose
def compress(pubKey):
    return hex(pubKey.x) + hex(pubKey.y % 2)[2:]

#Curve Selection
curve = registry.get_curve('secp192r1')
print("\nThe Curve Used is -> secp192r1 ")
print("\n-------------------------------------------------------------------")
print("\n\t\t\t PUBLIC KEYS")


#User A
APrivKey = secrets.randbelow(curve.field.n) #na
APubKey = APrivKey * curve.g #PA = na * G
print("\n\n\tUser 'A' public key:", compress(APubKey))


#User B
BPrivKey = secrets.randbelow(curve.field.n) #nb
BPubKey = BPrivKey * curve.g #PB = nb * G
print("\n\tUser 'B' public key:", compress(BPubKey))
print("\n---------------------------------------------------------------------")
print("\n\t\t\tNow exchange the public keys")
time.sleep(3)
print("\n---------------------------------------------------------------------")
print("\n\t\t\t Shared KEYS")


#Display Shared Key 'K'
ASharedKey = APrivKey * BPubKey #K = na * PB
print("\n\tUser 'A' Shared key:", compress(ASharedKey))
BSharedKey = BPrivKey * APubKey #K = nb* PA
print("\n\tUser 'B' Shared key:", compress(BSharedKey))
print("\n----------------------------------------------------------------------")