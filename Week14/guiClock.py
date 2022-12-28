# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 10:32:06 2022

@author: yang
"""

import tkinter as tk
import time
from math import sin,cos,pi

rw=tk.Tk()
h,m,s=0,0,0
canvas=tk.Canvas(rw,height=300,width=300)
canvas.pack()
hhl=50
mhl=75
shl=100
canvas.create_oval(40,40,260,260,width=2)
sendx,sendy=shl*cos((s-15)/30*pi),shl*sin((s-15)/30*pi)
sh= canvas.create_line(150,150,sendx+150,sendy+150,arrow=tk.LAST)
for i in range(60):
    x1,y1=110*cos(i/30*pi),110*sin(i/30*pi)
    if i%5==0:
        x2,y2=102*cos(i/30*pi),102*sin(i/30*pi)
        canvas.create_line(x1+150,y1+150,x2+150,y2+150,width=2)
    else:
        x2,y2=105*cos(i/30*pi),105*sin(i/30*pi)
        canvas.create_line(x1+150,y1+150,x2+150,y2+150)
                
def tic():
    global s
    sendx,sendy=shl*cos((s-15)/30*pi),shl*sin((s-15)/30*pi)
    canvas.coords(sh,150,150,sendx+150,sendy+150)
    s+=1
    rw.after(10,tic)
ctime=time.localtime()        
tic()
tk.mainloop()
