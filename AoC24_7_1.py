#6/10
def check(operandslist,length,out):
    if length==1:
        
        if operandslist[0]==str(out):
            
            return 1
        else:
            
            return 0
    if length>1:
        
        ele=int(operandslist[0])
        sum=ele+int(operandslist[1])
        prod=ele*int(operandslist[1])
        length-=1
        
        operandslistsum=operandslist.copy()
        operandslistsum[1]=str(sum)
        operandslistsprod=operandslist.copy()
        operandslistsprod[1]=str(prod)
        
        return check(operandslistsum[1:],length,out) + check(operandslistsprod[1:],length,out)
        
        
    
    
    
    

main=[]
while True:
    s=input()
    if not s:
        break
    else:
        main.append(s)
count=0
for i in main:
        arr=i.split(":")
        output=int(arr[0])
        
        operandslist=arr[1].strip().split(" ")
        length=len(operandslist)
        if check(operandslist,length,output)>0:
            
            
            count+=output
        
print(count)
       
        

            

