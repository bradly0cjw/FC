import math
while True:
    eval=float(input())
    num=int((math.log(abs(float(eval)),2))//1)
    # no need in this section 
    # denormalize=0
    # exponent=127+num
    # if num<-127:
    #     denormalize=exponent
    #     exponent=0
    # num2=int(((((abs(eval)/(2**(num-denormalize))))*(2**denormalize))%1)*(2**23))
    num2=int((((abs(eval)/(2**num)))%1)*(2**23)) 
    print(f'{num2:023b}')
    # num3=int((abs(eval))%1*(2**(23-num+denormalize)))
    # num2=(((abs(eval)/(2**(num-denormalize))))*(2**denormalize))%1
    # binary=[]
    # for i in range(0,23):
    #     num3=(num2*2//1,num2*2%1)
    #     num2=num3[1]
    #     binary.append(int(num3[0]))
    # x=''.join(str(x) for x in binary)
    # print(x)
