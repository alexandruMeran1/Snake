from turtle import Turtle
MOVE_DIST=20
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
class Snake:

    def __init__(self):
        self.snake_seg=[]
        self.create_snake()
        self.snake_head=self.snake_seg[0]

    def create_snake(self):
        for i in STARTING_POSITIONS :
            self.addsegment(i)

    def addsegment(self,pos):
        s = Turtle( shape="square" )
        s.color( "white" )
        s.penup( )
        s.goto(pos)
        self.snake_seg.append( s )

    def extend(self):
        self.addsegment(self.snake_seg[-1].position())


    def move(self):
        for i in range( len( self.snake_seg ) - 1 , 0 , -1 ) :
            self.snake_seg[i].goto( self.snake_seg[i - 1].xcor( ) , self.snake_seg[i - 1].ycor( ) )
        self.snake_head.forward( MOVE_DIST )

    def up(self):
        if self.snake_head.heading() != 270 :
            self.snake_head.setheading(90)
    def down(self):
        if self.snake_head.heading() != 90 :
            self.snake_head.setheading( 270 )
    def left(self):
        if self.snake_head.heading() != 0 :
            self.snake_head.setheading( 180 )
    def right(self):
        if self.snake_head.heading() != 180 :
            self.snake_head.setheading( 0 )
    def reset(self):
        for seg in self.snake_seg:
            seg.goto(1000,1000)
        self.snake_seg.clear()
        self.create_snake()
        self.snake_head=self.snake_seg[0]
