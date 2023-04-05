def keyMatrix(key,n):
    mat=[[0 for _ in range(n)]for _ in range(n)]
    k=0
    for i in range(n):
        for j in range(n):
            mat[i][j]=ord(key[k])-65
            k+=1
    return mat

def encrypt(s,key):
    n=len(s)
    mat=keyMatrix(key,n)

    result=[0 for _ in range(n)]
    for i in range(n):
        for j in range(1):
            for k in range(n):
                result[i]+=mat[i][k]*(ord(s[k])-65)
    ans=""
    for ele in result:
        ans+=chr(ele%26+65)
    return ans
            

s=input("Enter the string to be encrypted : ")
#k must be NxN
k=input("Enter the key of vernam : ")
new=encrypt(s,k)
print("The encrypted String is : " , new)
