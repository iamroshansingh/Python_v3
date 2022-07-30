"""
'''we are going to draw some pattern'''

for pattern in range (1,10):
     for col in range (1,10):
          print("*",end=' ')
     print(" ")
     
print(" ")


for pattern in range(1,10):
     for col in range (pattern,pattern+1):
          print ("*"*col)
     print()
"""
import turtle  
# Creating turtle  
t = turtle.Turtle()  
s = turtle.Screen()  
s.bgcolor("black")  
t.pencolor("red")  
  
a = 0  
b = 0  
t.speed(0)  
t.penup()  
t.goto(0,200)  
t.pendown()  
while(True):  
    t.forward(a)  
    t.right(b)  
    a+=3  
    b+=1  
    if b == 210:  
        break  
    t.hideturtle()  
  
turtle.done()  
