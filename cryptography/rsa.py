import math
p=7
q=11
n=p*q 
phi=((p-1)*(q-1))

e=2  
while e<phi:
    if math.gcd(e,phi)==1:
        break 
    e+=1

msg=int(input("Enter number of characters in message : "))

print("Encrypted Data is : ",pow(msg,e,n))
