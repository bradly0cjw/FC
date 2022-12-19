n=int(input())
while True:
    origin=[]
    stack=[]
    ck=1
    y=list(map(int,input().split(" ")))
    for i in range(0,len(y)):
        origin.append(i+1)
    while len(y)!=0:
        if len(origin)!=0:
            if y[0]==origin[0]:
                origin.pop(0)
                y.pop(0)
            else:
                if len(stack)!=0:
                    if y[0]==stack[-1]:
                        stack.pop()
                        y.pop(0)
                    else:
                        stack.append(origin[0])
                        origin.pop(0)
                else:
                    stack.append(origin[0])
                    origin.pop(0)
        else:
            if y[0]==stack[-1]:
                stack.pop()
                y.pop(0)
            else:
                print("no")
                ck=0
                break      
    if len(y)==0:
        print("yes")
    elif ck==1:
        print("no")
    