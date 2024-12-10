arr=[]
while True:
    s=input()
    if not s:
        break
    else:
        arr.append(s)

antinodes=[]
for i in range(len(arr)):
    for j in range(len(arr[0])):
        pos=arr[i][j]
        for p in range(i,len(arr)):
            for q in range(len(arr[0])):
                if p!=i and q!=j and arr[p][q]==arr[i][j] and arr[p][q]!="." and arr[p][q]!="#":
                    
                    try:
                        temp=arr[i-(p-i)][j-(q-j)]
                        
                        if [i-(p-i),j-(q-j)] not in antinodes and i-(p-i)>=0 and j-(q-j)>=0:
                            # print(i-(p-i),j-(q-j))
                            antinodes.append([i-(p-i),j-(q-j)])
                    except:
                        pass
                    try:
                        temp=arr[p+(p-i)][q+(q-j)]
                        
                        if [p+(p-i),q+(q-j)] not in antinodes and p+(p-i)>=0 and q+(q-j)>=0:
                            # print(p+(p-i),q+(q-j))
                            antinodes.append([p+(p-i),q+(q-j)])
                    except:
                        pass
                    

print(len(antinodes))
