def polyline(number,n,step_length,step_angle,angle):
    '''多边形'''
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
