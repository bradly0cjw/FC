def main():
    maxp=1000001
    li=[True]*maxp
    for i in range(2,int((maxp**0.5)+1)):
        if li[i]==True:
            li[i]=i
            for j in range(i*i,(maxp),i):
                if (li[j]==True):
                    li[j]=i
    for i in range(0,maxp):
        if li[i]==True:
            li[i]=i
    while True:
        k=int(input())
        print(k,end="=")
        out=[]
        li2=li[int(k)]
        while li2!=1:
            out.append(str(li2))
            k=k/li2
            li2=li[int(k)] 
        if len(out)==0:
            out.append(str(1))
        s="*".join(out)  
        print(str(s)) 
main()      