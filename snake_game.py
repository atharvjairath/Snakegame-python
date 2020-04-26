import turtle
import time
import random 
delay=0.12

#score
score=0
high_score=0


#setup screen
wn=turtle.Screen()
wn.title("SNAKE GAME BY AIR")
wn.bgcolor("green")
wn.setup(width=600,height=600)
wn.tracer(0) #turns off screen updation
#snake head
head=turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("Black")
head.penup()
head.goto(0,0)
head.direction="stop"
#funvtions

#snake food
food=turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)


#pen
pen=turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score:0 High Score: 0", align="center", font=("Courier",24,"normal"))
segements =[]

def move():
    if head.direction=='up':
        y=head.ycor()
        head.sety(y+20)
    if head.direction=='down':
        y=head.ycor()
        head.sety(y-20)
    if head.direction=='left':
        x=head.xcor()
        head.setx(x-20) 
    if head.direction=='right':
        x=head.xcor()
        head.setx(x+20)    


def go_up():
    if head.direction != "down":
         head.direction="up"
def go_down():
    if head.direction != "up":
        head.direction="down"  
def go_left():
    if head.direction != "right":
        head.direction="left"  
def go_right():
    if head.direction != "left":
        head.direction="right" 

#keyboard bindings
wn.listen()
wn.onkeypress(go_up,'Up')
wn.onkeypress(go_down,'Down')
wn.onkeypress(go_left,'Left')
wn.onkeypress(go_right,'Right')






# Main Game loop
while True:
    wn.update()

    #check for a collison with the border
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(0.5)
        head.goto(0,0)
        head.direction="stop"
        delay=0.12
        score=0
        pen.clear()
        pen.write("Score {} High Score: {}".format(score,high_score),align="center", font=("Courier",24,"normal")) 
       

        for seg in segements:
            seg.goto(1000,1000) 
        segements.clear()  

             

    if head.distance(food) < 20:
        #move the food to random spot
        x=random.randint(-280,280)
        y=random.randint(-280,280)
        food.goto(x,y)
        delay=delay - 0.002
        score+=10
        if score> high_score:
            high_score=score
        pen.clear()
        pen.write("Score {} High Score: {}".format(score,high_score),align="center", font=("Courier",24,"normal")) 

        # add a segement
        new_seg=turtle.Turtle()
        new_seg.speed(0)
        new_seg.shape("circle")
        new_seg.color("grey")
        new_seg.penup()
        segements.append(new_seg)
    #move the end segements first on reverse order
    for index in range(len(segements)-1,0,-1):
        x=segements[index-1].xcor()
        y=segements[index-1].ycor()
        segements[index].goto(x,y)

    # move segment 0 to where the head is
    if len(segements) > 0:
        x=head.xcor()
        y=head.ycor()
        segements[0].goto(x,y)    
    move()

    #body collison
    for seg in segements:
        if seg.distance(head) <20:
            time.sleep(1)
            head.goto(0,0)
            head.direction ="stop"
            delay=0.12
            score=0
            pen.clear()
            pen.write("Score {} High Score: {}".format(score,high_score),align="center", font=("Courier",24,"normal")) 
            for seg in segements:
                seg.goto(1000,1000) 
            segements.clear()             


    time.sleep(delay)




wn.mainloop()