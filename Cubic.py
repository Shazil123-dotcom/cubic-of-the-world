from turtle import*
tom = Turtle()

screen = Screen()
screen.tracer(False)
screen.bgcolor('#dff5ff')


tom.width(5)
tom.color("black")
tom.pu()
tom.goto(200,-20)
tom.pd()
tom.speed(500)
tom.begin_fill()
tom.color('black','#dabfad')
tom.rt(360/5)
tom.fd(120)
tom.bk(50)
tom.lt(360/7)
tom.fd(100)
tom.rt(360/3.75)
tom.fd(200)
tom.lt(-40)
tom.fd(200)

tom.rt(360/8.25)
tom.fd(200)
tom.setheading(0)
tom.lt(120)
tom.fd(200)
tom.rt(85)
tom.fd(100)
tom.rt(145)
tom.fd(70)
tom.fd(-150)

tom.rt(180-30)
tom.fd(100)
tom.fd(-100)

tom.rt(180)
for count in range(40):
    tom.lt(1)
    tom.fd(1)
tom.fd(150)

for count in range(40):
    tom.lt(1)
    tom.fd(1)

for count in range(40):
    tom.lt(1)
    tom.fd(1)
tom.fd(150)

for count in range(45):
    tom.lt(1)
    tom.fd(1)
tom.fd(100)
tom.end_fill()

for count in range(45):
    tom.rt(1)
    tom.fd(1)

for count in range(45):
    tom.lt(1)
    tom.fd(1)
tom.lt(-45)

for count in range(-45):
    tom.rt(1)
    tom.bk(1)
tom.lt(+45)

tom.pu()
tom.goto(-150,-250)
tom.pd()

tom.rt(90)
tom.fd(150)

for count in range(25):
     tom.rt(1)
     tom.fd(1)
tom.lt(25)
for count in range(65):
     tom.lt(1)
     tom.fd(1)
tom.lt(-65)

for count in range(-65):
     tom.rt(1)
     tom.bk(1)
tom.lt(+65)
tom.rt(60)
tom.fd(100)

tom.pu()
tom.goto(100,70)
tom.pd()
print(tom.heading())
print(tom.position())
tom.begin_fill()
tom.color('black','white')
tom.lt(20)
tom.fd(80)
tom.rt(115)
tom.fd(35)
tom.rt(90)
for count in range(25):
    tom.lt(1)
    tom.fd(3)
tom.rt(100)
tom.fd(16)    
tom.end_fill()

tom.rt(80)
tom.fd(40)

tom.begin_fill()
tom.color('black' , '#787474')
tom.setheading(0) 
tom.rt(90) 
tom.circle(-12,180)
tom.end_fill()  

tom.begin_fill()
tom.color('black' , '#989898')
tom.lt(180)
tom.fd(10)
tom.rt(80)
tom.fd(15)
tom.rt(170)
tom.fd(85)

for i in range(15):
    tom.rt(3.5)
    tom.fd(1)

tom.fd(-30)
tom.left(180)
for count in range(25):
    tom.lt(3)
    tom.fd(1) 
tom.lt(-15)      
tom.fd(60)
tom.lt(90)
tom.fd(20)
tom.end_fill()

tom.setheading(180)
tom.pu()
tom.goto(-50,70)
tom.pd()

tom.begin_fill()
tom.color('black','white')
tom.rt(20)  
tom.fd(80)
tom.lt(115)  
tom.fd(35)
tom.lt(90)  
for count in range(25):
    tom.rt(1) 
    tom.fd(3)
tom.lt(100)  
tom.fd(16)    
tom.end_fill()

tom.lt(80)  
tom.fd(40)

tom.begin_fill()
tom.color('black', '#787474')
tom.setheading(360) 
tom.fd(25)
tom.lt(90) 
tom.end_fill()

tom.begin_fill()
tom.color('black', '#989898')
tom.rt(180)  
tom.fd(10)
tom.lt(80) 
tom.fd(15)
tom.lt(170)  
tom.fd(85)

for i in range(15):
    tom.lt(3.5) 
    tom.fd(1)

tom.fd(-30)
tom.right(180) 
for count in range(25):
    tom.rt(3)  
    tom.fd(1) 
tom.rt(-15)  
tom.fd(60)
tom.rt(90)  
tom.fd(20)
tom.end_fill()







screen.tracer(True)
done()










