import turtle

STARTING_POSITION=[(0,0),(-20,0),(-40,0)]
DISTANCE=20
UP=90
DOWN=270
LEFT=180
RIGHT=0
class Snake:

    def __init__(self):
        self.segment=[]
        self.create_snake()
        self.head=self.segment[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self,position):
        new_segment=turtle.Turtle()
        new_segment.shape("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segment.append(new_segment)

    def extend(self):
        self.add_segment(self.segment[-1].position())

    def move(self):
        for i in range(len(self.segment)-1,0,-1):
            self.segment[i].goto(self.segment[i-1].xcor(),self.segment[i-1].ycor())

        self.segment[0].forward(DISTANCE)
    
    def up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading()!=UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading()!=RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading()!=LEFT:
            self.head.setheading(RIGHT)