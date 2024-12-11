#part2
arr=[]
count=0
while True:
    s=input()
    if not s:
        break
    else:
        arr.append(s)

for i in range(len(arr)):
    for j in range (len(arr[i])):
        
        try:
            if arr[i][j]=="M" and arr[i+1][j+1]=="A" and arr[i+2][j+2]=="S":
                if (arr[i][j+2]=="M" and arr[i+1][j+1]=="A" and arr[i+2][j]=="S") or (arr[i][j+2]=="S" and arr[i+1][j+1]=="A" and arr[i+2][j]=="M"):
                    count=count+1
        except:
            pass
        try:
            if arr[i][j]=="S" and arr[i+1][j+1]=="A" and arr[i+2][j+2]=="M":
                if (arr[i][j+2]=="M" and arr[i+1][j+1]=="A" and arr[i+2][j]=="S") or (arr[i][j+2]=="S" and arr[i+1][j+1]=="A" and arr[i+2][j]=="M"):
                    count=count+1
        except:
            pass
        
print(count)
            

