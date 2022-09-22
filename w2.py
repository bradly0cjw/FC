# def crazy():
birth = int(input())
var1 = birth % 10000
var2 = var1//100
var3 = var1 % 100
var4 = int(0)
opt = str("")
if (var2 > 9):
    var4 = var4+1
if ((var3 % 2) == 1):
     var4 = var4+2
if(var4 == 1):
    opt = ("科學麵")
elif(var4 == 2):
    opt = ("飲料")
elif(var4 == 3):
    opt = ("科學麵+飲料")
else:
    opt = ("0")
print(opt)

# while True:
#     crazy()
