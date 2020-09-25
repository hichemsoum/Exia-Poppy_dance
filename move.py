import time

def rest_pose(poppy,a):
    poppy.m1.goto_position(0, a, wait= True)
    poppy.m2.goto_position(0, a, wait= True)
    poppy.m4.goto_position(0, a, wait= True)
    poppy.m6.goto_position(0, a, wait= True)
    poppy.m3.goto_position(0, a, wait= True)
    poppy.m5.goto_position(0, a, wait= True)

def motor_test(poppy,m):
    if m==1:
        poppy.m1.goto_position(90,5)
    elif m==2:  
        poppy.m2.goto_position(90,5)
    elif m==3:  
        poppy.m3.goto_position(90,5)
    elif m==4:  
        poppy.m4.goto_position(90,5)
    elif m==5:  
        poppy.m5.goto_position(90,5)
    elif m==6: 
        poppy.m6.goto_position(90,5)

def skywatching(poppy):
   
    # poppy.m1.goto_position(0,5)
    # poppy.m2.goto_position(0,5)
    # poppy.m4.goto_position(0,5)
    # poppy.m6.goto_position(0,5)
    # poppy.m3.goto_position(-5, 5, wait= True)
    # poppy.m5.goto_position(-90, 5, wait= True)
    new_pose(poppy,0,0,-5,0,-90,0,5)
    time.sleep(3)
   
def reverse(poppy):
  
    # poppy.m1.goto_position(0,6)
    # poppy.m2.goto_position(0,6)
    # poppy.m4.goto_position(0,6)
    # poppy.m6.goto_position(0,6)
    # poppy.m3.goto_position(-90, 6, wait= True)
    # poppy.m5.goto_position(-90, 6, wait= True)
    new_pose(poppy,0,0,-90,0,-90,0,5)
    time.sleep(3)

def diver(poppy):
    # poppy.m1.goto_position(0,6)
    # poppy.m2.goto_position(-45, 6, wait= True)
    # poppy.m4.goto_position(0,6)
    # poppy.m6.goto_position(0,6)
    # poppy.m3.goto_position(45,6)
    # poppy.m5.goto_position(-45, 6, wait= True)
    new_pose(poppy,0,-45,45,0,-45,0,5)
    time.sleep(3)   

def balai(poppy):
    poppy.m2.goto_position(80, 6, wait= True)
    poppy.m5.goto_position(-90, 6, wait= True)
    poppy.m6.goto_position(0,6)
    poppy.m3.goto_position(0,6)
    poppy.m4.goto_position(0,6)
    poppy.m1.goto_position(180, 6, wait= True)
    poppy.m1.goto_position(-180, 6,wait= True)
   
def shaker(poppy):
    poppy.m1.goto_position(0, 2)
    poppy.m3.goto_position(0, 2)
    poppy.m2.goto_position(0, 2)
    poppy.m4.goto_position(0, 2)
    poppy.m5.goto_position(0, 2,wait= True)

    poppy.m1.goto_position(360, 20)
    while poppy.m1.present_position<=360 :
        poppy.m5.goto_position(-90, 3,wait= True)
        poppy.m5.goto_position(90, 2,wait= True)   
   
def init_loop(poppy):
    new_pose(poppy,0,-90,90,0,-180,0,10)

def loop(poppy):
    init_loop(poppy)
   # poppy.m2.goto_position(-45, 6, wait= True)
   # poppy.m3.goto_position(45, 6, wait= True)
   # poppy.m5.goto_position(-540, 5, wait= True)
   # poppy.m3.goto_position(90, 5, wait= True)
   # poppy.m2.goto_position(-90, 5, wait= True)
    poppy.m4.goto_position(360,6,wait=True)

def little_dance(poppy):
    balai(poppy)
    reverse(poppy)
    shaker(poppy)
    skywatching(poppy)
    loop(poppy)
    diver(poppy)
    rest_pose(poppy,3)

def new_pose(poppy,m1,m2,m3,m4,m5,m6,a):
    poppy.m1.goto_position(m1, a)
    poppy.m2.goto_position(m2, a)
    poppy.m3.goto_position(m3, a)
    poppy.m4.goto_position(m4, a)
    poppy.m5.goto_position(m5, a)
    poppy.m6.goto_position(m6, a)
