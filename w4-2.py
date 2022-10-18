import math
while True:
    binary=[]
    denormalize=0
    eval=float(input())
    num=int((math.log(abs(float(eval)),2))//1)
    exponent=127+num
    if num<-127:
        denormalize=exponent
        exponent=0
    num2=(((abs(eval)/(2**(num-denormalize))))*(2**denormalize))%1

    # for i in range(0,23):
    #     num3=(num2*2//1,num2*2%1)
    #     num2=num3[1]
    #     binary.append(int(num3[0]))
    # x=''.join(str(x) for x in binary)
    # print(x)