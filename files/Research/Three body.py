
import numpy as np
import matplotlib.pyplot as plt
import numpy as pd
import matplotlib.animation as animation
from datetime import datetime
from time import time


G=1
Ma=1
Mb=1
Mc=1
dt=0.0001
xa=-0.97000436
ya=0.24308753
xb=0.97000436
yb=-0.24308753
xc=0
yc=0

axv0=-0.93240737/2
ayv0=-0.86473146/2
bxv0=axv0
byv0=ayv0
cxv0=0.93240737
cyv0=0.86473146
    
dots = [[],[]]
dots1=[[],[]]
dots2=[[],[]]

t=0
while True:
    rab=abs((((xb-xa)**2)+((ya-yb)**2))**1.5)
    rac=abs((((xc-xa)**2)+((ya-yc)**2))**1.5)
    rbc=abs((((xb-xc)**2)+((yc-yb)**2))**1.5)
    
    
    wabx=G*Mb*(xb-xa)
    wacx=G*Mc*(xc-xa)
    wbax=G*Ma*(xa-xb)
    wbcx=G*Mc*(xc-xb)
    wcax=G*Ma*(xa-xc)
    wcbx=G*Mb*(xb-xc)
  
    waby=G*Mb*(yb-ya)
    wacy=G*Mc*(yc-ya)
    wbay=G*Ma*(ya-yb)
    wbcy=G*Mc*(yc-yb)
    wcay=G*Ma*(ya-yc)
    wcby=G*Mb*(yb-yc)

    cax=(wabx/(rab))+(wacx/(rac))
    cay=(waby/(rab))+(wacy/(rac))

    cbx=(wbax/(rab))+(wbcx/(rbc))
    cby=(wbay/(rab))+(wbcy/(rbc))

    ccx=(wcax/(rac))+(wcbx/(rbc))
    ccy=(wcay/(rac))+(wcby/(rbc))
    

    xa=-0.5*cax*dt**2+axv0*dt+xa
    ya=-0.5*cay*dt**2+ayv0*dt+ya
    
    
    xb=-0.5*cbx*dt**2+bxv0*dt+xb
    yb=-0.5*cby*dt**2+byv0*dt+yb
   
    xc=-0.5*ccx*dt**2+cxv0*dt+xc
    yc=-0.5*ccy*dt**2+cyv0*dt+yc
    
    axv0=axv0+cax*dt
    ayv0=ayv0+cay*dt
    bxv0=bxv0+cbx*dt
    byv0=byv0+cby*dt
    cxv0=cxv0+ccx*dt
    cyv0=cyv0+ccy*dt

    dots[0].append(xa)
    dots[1].append(ya)
    dots1[0].append(xb)
    dots1[1].append(yb)
    dots2[0].append(xc)
    dots2[1].append(yc)
    
    t+=dt
        
    if t>=6.35:break
    
plt.title('three body')        
plt.xlabel('x')
plt.ylabel('y')
plt.plot(dots[0],dots[1], 'r*')
plt.plot(dots1[0],dots1[1],'b*')
plt.plot(dots2[0],dots2[1],'y*')
plt.show()
plt.title('mass 1')
plt.xlabel('x')
plt.ylabel('y')
plt.plot(dots[0],dots[1], 'r*')
plt.show()
plt.title('mass 2')
plt.xlabel('x')
plt.ylabel('y')
plt.plot(dots1[0],dots1[1],'b*')
plt.show()
plt.title('mass 3')
plt.xlabel('x')
plt.ylabel('y')
plt.plot(dots2[0],dots2[1],'y*')
plt.show()

#animation

import matplotlib.animation as animation

fig = plt.figure()
ax=fig.add_subplot(111,autoscale_on=False , xlim=(-1.7,1.7) , xlabel=('x')  , ylim=(-0.8,0.8) , ylabel=('y'))
ax.set_aspect('equal')
ax.grid()
line1,=ax.plot([],[],'r.',marker=".",markersize=24,linestyle="")
line2,=ax.plot([],[],'b.',marker=".",markersize=24,linestyle="")
line3,=ax.plot([],[],color='black')
line4,=ax.plot([],[],color='black')
line5,=ax.plot([],[],'y.',marker=".",markersize=24,linestyle="")
line6,=ax.plot([],[],color='black')
M=80
time_text=ax.text(0.05,0.9,'',transform=ax.transAxes)
def init():
    time_text.set_text('')
    return time_text

def animate(i):
    i*=M
    time_text.set_text('time=%.1f'% i)
    r=[dots[0][i],dots[1][i]]
    r1=[dots1[0][i],dots1[1][i]]
    r2=[dots2[0][i],dots2[1][i]]
    line1.set_data(r[0],r[1])
    line3.set_data(dots[0][:i],dots[1][:i])
    line2.set_data(r1[0],r1[1])
    line4.set_data(dots1[0][:i],dots1[1][:i])
    line5.set_data(r2[0],r2[1])
    line6.set_data(dots2[0][:i],dots2[1][:i])
    return line1, line2, line3,time_text
t0=time()
animate(0)
t1=time()
interval =100*dt-(t1-t0)

ani=animation.FuncAnimation(fig,animate,int(len(dots[0])/M) ,interval=1)
plt.show()
