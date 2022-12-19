# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
class Node:

    def __init__(self,data):
        self.data=data
        self.link=None

def searchLinkedList(lkList,target):
    pre=None
    cur=lkList
    while cur!=None and target>cur.data:
        pre=cur
        cur=cur.link
    if cur!=None and cur.data==target:
        flag=True
    else:
        flag=False
    return pre,cur,flag
   
def insertLinkedList(lkList,target,node):
    pre,cur,flag=searchLinkedList(lkList,target)
    if flag:
        return lkList
    if lkList==None:
        lkList=node
        return lkList
    if pre==None:
        node.link=cur
        lkList=node
        return lkList
    if cur==None:
        pre.link=node
        node.link=None
        return lkList
    node.link=cur
    pre.link=node
    return lkList

def deleteLinkedList(lkList,target):
    pre,cur,flag=searchLinkedList(lkList,target)
    if flag==False:
        return lkList
    if pre==None:
        lkList=cur.link
        return lkList
    pre.link=cur.link
    return lkList

def traverseLinkedList(lkList):
    cur=lkList
    while cur!=None:
        print(cur.data,end=" ")
        cur=cur.link
    print()

myList=None
for i in range(10):
    node=Node(i)
    myList=insertLinkedList(myList,i,node)
traverseLinkedList(myList)

myList=deleteLinkedList(myList,4)
traverseLinkedList(myList)




