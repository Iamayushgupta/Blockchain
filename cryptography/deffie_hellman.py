P=int(input("Enter the value of prime number : "))
G=int(input("Enter the value of primitive root of prime number : "))

a=int(input("Enter the private key of Alice : "))

x = int(pow(G,a,P))
print("The generated key of Alice is",x)

b=int(input("Enter the private key of Bob : "))

y = int(pow(G,b,P))
print("The generated key of Bob is",y)

#Secret Key of Alice
ka = int(pow(y,a,P))

#Secret key of Bob
kb = int(pow(x,b,P))

print("Secret key of Alice is",ka)
print("Secret key of Bob is",kb)
