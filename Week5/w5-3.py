import collections
def main():
    maxp=1000000
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
        k=j=input()
        out=[]
        v=1
        li2=li[int(k)]
        while li2!=1:
            out.append(str(li2))
            k=int(k)/li2
            li2=li[int(k)] 
        # if len(out)<1:
        #     out.append(str(1))
        n=list(set(out))
        for m in n:
            v=v*(collections.Counter(out)[m]+1)  
        print(v) 
main()