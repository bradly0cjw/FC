a=input()
a=list(map(int,a.split(" ")))
global bstarray
bstarray=[]
class Node:
    def __init__(self,key):
        self.key=key
        self.lptr=None
        self.rptr=None
def preorderTraverse(tree):
    if tree!=None:
        print(tree.key)
        preorderTraverse(tree.lptr)
        preorderTraverse(tree.rptr)
def searchBST(tree,target):
    if tree==None:
        return False
    if tree.key>target:
        searchBST(tree.lptr,target)
    elif tree.key<target:
        searchBST(tree.rptr,target)
    else:
        return True
def insertBST(tree,target):
    if tree==None:
        tree=Node(target)
        return tree
    if tree.key>target:
        tree.lptr=insertBST(tree.lptr,target)
    elif tree.key<target:
        tree.rptr=insertBST(tree.rptr,target)
    return tree
def maxbst(tree):
    if tree==None:
        return 0
    return(max(1+maxbst(tree.rptr),1+maxbst(tree.lptr)))
def bsttoarray(tree,num):
    if tree==None:
        return None
    if tree.key==None:
        return None
    bstarray[num]=(tree.key)
    bsttoarray(tree.lptr,2*(num))
    bsttoarray(tree.rptr,2*(num)+1)
    return bstarray
    pass
bst=None
# a=[8,3,1,6,4,7,10,14,13]
# a=[9,5,10,3,6,14]
arraylength=0
for i in a:
    bst=insertBST(bst,i)
length=maxbst(bst)
for k in range(0,length):    
    arraylength=arraylength+2**k
bstarray=[None]*(arraylength+1)
bsttoarray(bst,1)
base=arraylength-2**(length-1)
for j in range(1,2**(length-1)+1):
    calc=base+j
    temparray=[]
    if bstarray[calc]!=None:
        temparray.append(bstarray[calc])
    while calc!=1:
        if (calc%2)!=0:
            calc=calc-1
        calc=int(calc/2)
        if bstarray[calc]==None:
            break
        temparray.append(bstarray[calc])
    if len(temparray)==length:
        for i in range(len(temparray)-1,0,-1):
            print(temparray[i],end=" ")
        print(temparray[0])
# def heightBST(tree):
#     if tree==None:
#         return 0
#     if tree.lptr==None and tree.rptr==None:
#         return 0
#     elif tree.lptr==None:
#         return heightBST(tree.rptr)+1
#     elif tree.rptr==None:
#         return heightBST(tree.lptr)+1
#     if heightBST(tree.lptr)>heightBST(tree.rptr):
#         return heightBST(tree.lptr)+1
#     else:
#         return heightBST(tree.rptr)+1    
