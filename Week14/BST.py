# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 17:41:38 2022

@author: user
"""
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
        
global stack,sp,height
stack=[]
sp=-1       
def DFS(tree):
    if tree!=None:
        stack.push(tree.key)
        sp=sp+1
        if sp==height:
            for i in range(len(stack)):
                print(stack[i],end='')
                if i==len(stack):
                    print()
                else:
                    print(' ',end='')
            stack.pop()
            sp=sp-1
        if tree.lptr!=None:
            DFS(tree.lptr)
        elif tree.rptr!=None:
            DFS(tree.rptr)
        else:
            
        
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
        tree=Node(target);
        return tree
    elif tree.key>target:
        tree.lptr=insertBST(tree.lptr,target)
        return tree
    elif tree.key<target:
        tree.rptr=insertBST(tree.rptr,target)
        return tree
    else:
        return tree

def treeDepth(tree):
    if tree==None:
        return 0
    else:
        return max(1+treeDepth(tree.lptr),1+treeDepth(tree.rptr))
    
tree=None
data=list(map(int,input().split()))
for t in data:
    tree=insertBST(tree,t)

height=treeDepth(tree)-1
