#part_2
import math
arrl=[]
arrr=[]
while True:
    value =input()
    if not value:
        break
    split=value.split()
    arrl.append(int(split[0]))
    arrr.append(int(split[1]))
    
sum=0
for i in arrl:
    count=0
    for j in arrr:
        if(i==j):
            count+=1
    sum+=(i*count)
print(sum)
