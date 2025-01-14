import math
import time

print("\n\t\t Inputs")
p = int(input("\nEnter the prime no. p ->"))
q = int(input("\nEnter the prime no. q ->"))

#Enter the private keys
a = int(input("\nEnter private key of user A ->"))
b = int(input("\nEnter private key of user B ->"))

print("\n---------------------------------------------")

#Now generate the public key

pa = math.fmod((q**a),p)
pb = math.fmod((q**b),p)

print("\n\n\nOutput")
print("\nPrivate key of A is ->"+str(a))
print("\nPrivate key of B is ->"+str(b))
print("\n Public key generated of A is ->"+str(pa))
print("\nPublic key generated of B is ->"+str(pb))

print("\n========================================")
print("\n\t Exchanging Keys , Please wait....")
time.sleep(3)

# Now Exchnage the keys and calculate it(variables are Ea and Eb)

Ea = math.fmod((pb**a),p)
Eb = math.fmod((pa**b),p)

print("\n Exchanged keys of A is ->"+str(Ea))
print("\n Exchanged keys of B is ->"+str(Eb))

if Ea==Eb:
    print("\n Key Exchanging successfully took place")
