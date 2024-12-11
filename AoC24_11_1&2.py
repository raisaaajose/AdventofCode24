import re
s=input()
arr=s.split(" ")
#for part 2 switch 25 with 75 :)
for i in range(0,25):
    arr_new=[]
    for j in arr:
        if j=="0":
            arr_new.append("1")
        elif len(j)%2==0:
            arr_new.append(j[0:int(len(j)/2)])
            pattern=r"^0+"
            if re.fullmatch(pattern,j[int(len(j)/2):]):
                arr_new.append("0")
            elif re.match(pattern,j[int(len(j)/2):]):
                arr_new.append(j[int(len(j)/2):].lstrip("0"))
            else:
                arr_new.append(j[int(len(j)/2):])
        else:
            arr_new.append(str(int(j)*2024))
    
    arr=arr_new.copy()

print(len(arr))
