arr=[]
while True:
    s=input()
    if not s:
        break
    else:
        arr.append(s)
guardX=0
guardY=0
for i in range(len(arr)):
    for j in range(len(arr[0])):
        if arr[i][j]=="^":
            guardX=j
            guardY=i

count=1
arrpos=[[guardY,guardX]]
dir="up"
try: 
    while True:
        
        if dir=="up":
            
            if arr[guardY-1][guardX]!="#":
                guardY-=1
                # print("moving up")
                if([guardY,guardX] not in arrpos):
                    count+=1
                    arrpos.append([guardY,guardX])
            else:
                dir="right"
                # print("moving up to right")

        elif dir=="right":
            
            if arr[guardY][guardX+1]!="#":
                guardX+=1
                # print("moving right")
                if([guardY,guardX] not in arrpos):
                    count+=1
                    arrpos.append([guardY,guardX])
            else:
                
                dir="down"
                # print("moving right to down")
        elif dir=="down":
            
            if arr[guardY+1][guardX]!="#":
                guardY+=1
                # print("moving down")
                if([guardY,guardX] not in arrpos):
                    count+=1
                    arrpos.append([guardY,guardX])
                
            else:
                
                dir="left"
                # print("moving down to left")
        elif dir=="left":
            
            if arr[guardY][guardX-1]!="#":
                guardX-=1
                # print("moving left")
                if([guardY,guardX] not in arrpos):
                    count+=1
                    arrpos.append([guardY,guardX])
            else:
                
                dir="up"
                # print("moving left to up")
        
            
        
        
except:
    pass
print(count)
