def loop():
    n=int(input())
    s=0
    for i in range(1,n+1):
       s=s+i**2
    if n!=-1:
        print(s)

while True:
    loop()
   