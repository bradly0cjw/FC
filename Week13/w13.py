# a=input()
# a=list(map(int,a.split("  ")))
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
a=[9,5,3,6,10,13]
bst=None
for i in a:
    bst=insertBST(bst,i)
preorderTraverse(bst)