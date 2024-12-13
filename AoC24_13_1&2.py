arr=[]
while True:
    s=input()
   
    if s=="p":
            
            break
    else:
           arr.append(s)

def solve(part):
    tokens = 0
    if part == 2:
        add = 10000000000000 
    else:
        add=0
    for s in range(0,len(arr),4):
        if arr[s]!="":
            x1=int(arr[s][12]+arr[s][13])
            y1=int(arr[s][-2]+arr[s][-1])
            x2=int(arr[s+1][12]+arr[s+1][13])
            y2=int(arr[s+1][-2]+arr[s+1][-1])
            temp=arr[s+2].split("=")
            y_final=int(temp[-1])+add
            t=temp[1].split(",")
            x_final=int(t[0])+add
            a = (x_final*y2 - y_final*x2) / (x1*y2 - y1*x2)
            b = (y_final*x1 - x_final*y1) / (x1*y2 - y1*x2)
            if a == int(a) and b == int(b):
                tokens += int(3 * a + b)

    print(tokens)

solve(1)
solve(2)
