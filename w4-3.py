import math
while True:
    # binary=[]
    # expon=[]
    denormalize=0
    eval=float(input())
    num=int((math.log(abs(float(eval)),2))//1)
    exponent=127+num
    if num<-127:
        denormalize=exponent
        exponent=0
    num2=(((abs(eval)/(2**(num-denormalize))))*(2**denormalize))%1
    # x=(f'{num2:123b}') 
    y=(f'{exponent:08b}')
    # for i in range(0,8):
    #     calc=(exponent//(2**(7-i)),exponent%(2**(7-i)))
    #     expon.append(int(calc[0]))
    #     exponent=calc[1]
    # y=''.join(str(y) for y in expon)
    if (eval<0):
        sign='1'
    else:
        sign='0'
    print(sign+y,end="")
    # for i in range(0,23):
    #     num3=(num2*2//1,num2*2%1)
    #     num2=num3[1]
    #     print(int(num3[0]),end="")
    #     binary.append(int(num3[0]))
    # x=''.join(str(x) for x in binary)
    print()
