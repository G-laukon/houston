import turtle
import math
t = turtle.Turtle()
t.hideturtle()

def draw_a():
    t.reset()
    t.pensize(7)
    t.hideturtle()
    angle = math.asin(100/110)/(2*math.pi)*360  
    t.lt(float(angle))
    t.fd(55)
    cross_pos1 = t.pos()
    t.fd(55)
    t.rt(2*float(angle))
    t.fd(55)
    cross_pos2 = t.pos()
    t.fd(55)
    t.penup()
    t.goto(cross_pos1)
    t.seth(0)
    t.pendown()
    t.goto(cross_pos2)

def draw_b():
    t.reset()
    t.pensize(7)
    t.hideturtle()
    angle_step = 180/10
    length_step = math.pi*25/10
    t.lt(90)
    t.fd(100)
    t.rt(90)
    t.fd(10)
    for i in range(10):
            t.rt(angle_step)
            t.fd(length_step)
    t.rt(180)
    t.fd(15)
    for i in range(10):
            t.rt(angle_step)
            t.fd(length_step)
    t.fd(10)



def draw_c():
    t.reset()
    t.pensize(7)
    t.hideturtle()
    angle = 170
    l = 100
    r = l/2/math.sin(math.radians(angle/2))
    arc = r*math.radians(angle)
    h = l/2/math.tan(math.radians(angle/2))
    
    t.penup()
    t.goto(0,(r-h))
    t.lt(180-angle/2)
    t.pendown()
      
    for i in range(30):
        t.fd(int(arc/30))
        t.rt(float(angle/30))

    t.penup()
    t.home()
    t.goto(0,(r-h))
    t.rt(90)
    t.pendown()
    t.fd(100-2*(r-h))
    
    for i in range(30):
        t.fd(int(arc/30))
        t.lt(float(angle/30))



def draw_d():
    t.reset()
    t.pensize(7)
    t.hideturtle()
    angle = 180
    r = 50
    arc = math.pi*r

    t.fd(12)
      
    for i in range(50):
        t.fd(int(arc/50))
        t.lt(float(angle/50))

    t.fd(15)
    t.lt(90)
    t.fd(92)


def draw_e():
    t.reset()
    t.pensize(7)
    t.hideturtle()
    
    t.lt(89)
    t.fd(100)
    t.rt(90)
    t.fd(55)
    t.penup()
    t.home()
    t.pendown()
    t.fd(55)
    t.penup()
    t.goto(1,50)
    t.pendown()
    t.fd(55)
