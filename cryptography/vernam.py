# Works only for Capital Alphabets
def encrypt(s,key):
    ans=""
    n=len(s)
    for i in range(n):
        a=ord(s[i])-65
        b=ord(key[i])-65
        x=a^b 
        ans+=chr(x%26 + 65)
    return ans

s=input("Enter the string to be encrypted : ")
k=input("Enter the key of vernam : ")
new=encrypt(s,k)
print("The encrypted String is : " , new)