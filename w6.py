# the following is the skeleton code segment…. 
memory=[0 for i in range(254)] # 記憶體 254 words
register=[0 for i in range(16)] # 暫存器 16 個
pc=0 #程式記數器 program counter
ir=0 #指令暫存器 Instruction Register
noi=int(input())        # 讀入指令數 
for i in range(noi):    # load instructions to memeory
   memory[i]=int(input(),16) # instruction以16進位讀入

while True:          # machine cycle 機器循環
    ir=memory[pc]     # 指令抓取 fetch instruction
    opcode=ir>>12   # 解碼 取得op code 
    Rd=(ir>>8)%(2**4)  # 取得 Rd 目的地暫存器 ,Rs1 來源暫存器1 ,Rs2 來源暫存器2
    Rs1=(ir>>4)%(2**4)
    Rs2=(ir)%(2**4)
    Md=(ir>>4)%(2**8)   # Ms 來源記憶體位址, Md 目的地記憶體位址
    Ms=(ir)%(2**8)
    pc=pc+1         # pc 指向下一指令所在位址
    # print(f"{ir:b},{opcode:b},{Rd:b},{Rs1:b},{Rs2:b},{Ms:b},{Md:b}",pc)
    if opcode==0:      # 解碼執行指令碼 (參考指令表)
        break
    elif opcode==1:
        try:
            register[Rd]=memory[Ms]
        except:
            register[Rd]=input()
    elif opcode==2:
        try:
            memory[Md]=register[Rs2]
        except:
            print(register[Rs2])    
    elif opcode==3:
        register[Rd]=register[Rs1]+register[Rs2]
    elif opcode==4:
        register[Rd]=register[Rs1]+register[Rs2]
    elif opcode==5:
        register[Rd]=register[Rs1]
    elif opcode==6:
        register[Rd]=~register[Rs1]
    elif opcode==7:
        register[Rd]=register[Rs1]&register[Rs2]
    elif opcode==8:
        register[Rd]=register[Rs1]|register[Rs2]
    elif opcode==9:
        register[Rd]=register[Rs1]&register[Rs2]
    elif opcode==10:
        register[Rd]=register[Rd]+1
    elif opcode==11:
        register[Rd]=register[Rd]-1
    elif opcode==12:
        rot=[]
        rot=(register[Rd])
        n=len(rot)
        if register[Rs2]==0:
            first=rot[n-int(register[Rs1]):]
            last=rot[:n-int(register[Rs1])]
        else:
            first=rot[int(register[Rs1])-n:]
            last=rot[:int(register[Rs1])-n]
        register[Rd]=(first+last)
    elif opcode==13:
        if register[0]!= register[Rd]:
            pc=register[Rs1]
    elif opcode==14:
        register[Rd]=input()
    elif opcode==15:
        print(register[Rs2])
    else:
        break
# 0001 0001 1111 1110
# 0010 1111 1111 0001
# 0000 0000 0000 0000
