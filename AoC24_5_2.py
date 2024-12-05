#part2
order=[]
temp=[]
while True:
    s=input()
    if not s:
        break
    else:
         order.append(s.split("|"))
while True:
    s=input()
    if not s:
        break
    else:
         temp.append(s.split(","))

sum=0
for record in temp:
    flag=0
    while True:
        flag2=0
        for ele in record:
            for comp in order:
                if comp[0]==ele:
                    if comp[1] in record:
                        if record.index(comp[1])<record.index(comp[0]):
                            record[record.index(comp[0])]=comp[1]
                            record[record.index(comp[1])]=comp[0]
                            flag=1
                            flag2=1
                
                if comp[1]==ele:
                    if comp[0] in record:
                        if record.index(comp[1])<record.index(comp[0]):
                            record[record.index(comp[0])]=comp[1]
                            record[record.index(comp[1])]=comp[0]
                            flag=1   
                            flag2=1  
        if flag2==0:
            break                             
    if flag==1:
        sum+=int(record[int((len(record))/2)])
print(sum)
