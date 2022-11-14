maxp=10
li=[True]*maxp
for i in range(2,int((maxp-1)**0.5)):
    if li[i]:
        for j in range(i*i,(maxp),i):
            li[j]=False
print(li)