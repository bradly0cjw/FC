# regiester=[0 for i in range(16)]
# memory=[0 for i in range(256)]
# ir=32
# print(f'{ir:032b}')
a=(0xC50000000)
b=(0x7ffff)
print((a&b)/2**23+1)