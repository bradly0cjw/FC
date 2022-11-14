def main():
    maxp=1000000
    li=[True]*maxp
    for i in range(2,int((maxp**0.5)+1)):
        if li[i]==True:
            li[i]=i
            for j in range(i*i,(maxp),i):
                if (li[j]==True):
                    li[j]=i
    # for i in range(0,maxp):
    #     if li[i]==True:
    #         li[i]=i
    while True:
        k=input().split()
        o=[]
        for l in k:
            if li[int(l)]==True:
                li[int(l)]=l
            o.append(str(li[int(l)]))
        s=" ".join(o)  
        print(s)
main()
# print(li[int(k)],k)
# for i in range(2,maxp):
#     if li[i]:
#         print (i,end="") 
#correct
