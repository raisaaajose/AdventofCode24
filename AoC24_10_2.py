arr=[]
while True:
    s=input()
    if not s:
        break
    else:
        arr.append(s)

def check(i,j,n):
    if arr[i][j]=="9":
        return 1
    ls=0
    rs=0
    us=0
    ds=0
    try:
        if j-1 >=0 and arr[i][j-1]==str(n+1):
            ls=check(i,j-1,n+1)
    except:
        pass
    try:
        if arr[i][j+1]==str(n+1):
            rs=check(i,j+1,n+1)
    except:
        pass
    try:
        if arr[i+1][j]==str(n+1):
            ds=check(i+1,j,n+1)
    except:
        pass
    try:
        if i-1>=0 and arr[i-1][j]==str(n+1):
            us=check(i-1,j,n+1)
    except:
        pass
    # print(arr[i][j],i,j,ls,rs,us,ds)
    return ls+ds+us+rs


sum=0
for i in range(len(arr)):
    for j in range(len(arr[0])):
        if arr[i][j]=="0":
            sum+=check(i,j,0)
print(sum)
