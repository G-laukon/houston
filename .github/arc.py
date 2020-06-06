def arc(number,length,angle):
    """绘出花朵图案。三个输入参数分别决定瓣数，瓣长，瓣幅。ps:(10，100，200)效果不错。"""
    import math
    angle_arc = 2*math.pi*(angle/360)
    r = length/(2*math.sin(angle_arc/2))
    arc_length = angle_arc* r 
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle/2) / n
    polyline(number,n, step_length, step_angle,angle)
    

def polyline(number,n,step_length,step_angle,angle):
    import turtle
    t = turtle.Turtle()
    for i in range(number):
        for i in range(n):
            t.fd(step_length)
            t.lt(step_angle)

        t.rt(angle/2)

        for i in range(n):
            t.backward(step_length)
            t.lt(step_angle)

        t.lt(360/number-angle/2)
