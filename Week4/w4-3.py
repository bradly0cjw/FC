import math
while True:
    eval=float(input())
    num=int((math.log(abs(float(eval)),2))//1)
    exponent=127+num
    if num<-127:
        denormalize=exponent
        exponent=0
    else:
        denormalize=0
    num2=int(((abs(eval)/(2**(num-(2*denormalize))))%1)*(2**23))
    # num4=int(((abs(eval))*(2**(23))))
    # x=(f'{num2:023b}') 
    # z=(f'{num3:023b}')
    # y=(f'{exponent:08b}')
    if (eval<0):
        sign='1'
    else:
        sign='0'
    print(sign+f'{exponent:08b}'+f'{num2:023b}')
    # binary=[]
    # expon=[]
    # for i in range(0,8):
    #     calc=(exponent//(2**(7-i)),expon-ent%(2**(7-i)))
    #     expon.append(int(calc[0]))
    #     exponent=calc[1]
    # y=''.join(str(y) for y in expon)
    # for i in range(0,23):
    #     num3=(num2*2//1,num2*2%1)
    #     num2=num3[1]
    #     print(int(num3[0]),end="")
    #     binary.append(int(num3[0]))
    # x=''.join(str(x) for x in binary)
