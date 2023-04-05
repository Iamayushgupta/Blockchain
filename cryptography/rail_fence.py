def encrypt(s,key):
    n=len(s)
    matrix=[[0 for _ in range(n)] for _ in range(key)]
    bool=False
    i=0
    j=0
    for k in range(n):
        matrix[i][j]=s[k]
        k+=1
        if i==0 or i==key-1:
            bool=not bool
        
        if bool:
            i+=1
        else:
            i-=1
        j+=1

    ans=""
    for i in range(key):
        for j in range(n):
            if matrix[i][j]!=0:
                ans+=matrix[i][j]
    return ans


s=input("Enter the string to be encrypted : ")
k=int(input("Enter the key value of rail fence : "))
new=encrypt(s,k)
print("The encrypted String is : " , new)