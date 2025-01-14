import math

print("\n------------------------------------------------------")
print("\n\t\t\t INPUT VALUES")
p = int(input("\n\tEnter First Prime NO. 'p' -> "))
q = int(input("\n\tEnter Second Prime NO. 'q'-> "))
print("\n------------------------------------------------------\n")
m = int(input("\n\tEnter the Message to Cypher -> "))
print("\n------------------------------------------------------\n")


# cal n and phi(n)
n = p*q
phin = (p-1)*(q-1)


#for finding e
e= 0
for i in range(2,phin):
    if((math.gcd(i,phin)==1)):
        e= i
        break

#for finding d
d = 1
for i in range(e,phin):
    if((math.fmod((i*e),phin)==1)):
        d = i
        break


#ciypher text
c = int(math.fmod((m**e),n))
print("\n\n\n\n------------------------------------------------\n")
print("\n\t\t\t Output VALUES")
print("\n\tFollowing is the Cypher Text 'c'-> ",c)
print("\n-------------------------------------------------------\n")
#decrypt
decrypt = ints( math.fmod((c**d),n))
print("\n\tFollowing is the decyphered message -> ",decrypt)
print("\n--------------------------------------------------------\n")