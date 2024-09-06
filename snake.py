from tkinter import *
import random

W=700
H=600
S=80
SS=20
BP=3 
SC="blue"
FC="red"
BC="black"
class Snake:
    def __init__(self):
        self.body = BP
        self.coordinates =[]
        self.squares=[]
        for i in range(0,BP):
            self.coordinates.append([0,0])
        for x,y in self.coordinates:
            sq= canvas.create_rectangle(x,y,x+SS,y+SS,fill=SC,tag="snake")
            self.squares.append(sq) 

class Food:
    def __init__(self):
        x=random.randint(0,(W/SS)-1)*SS
        y=random.randint(0,(H/SS)-1)*SS
        self.coordinates=[x,y]
        canvas.create_oval(x,y,x+SS,y+SS,fill=FC,tag="food")
        
def nextT(snake,food):
    x, y=snake.coordinates[0]
    if direction == 'up':
        y -= SS
    elif direction == 'down':
        y += SS
    elif direction == 'left':
        x -= SS
    elif direction == 'right':
        x += SS
        
    snake.coordinates.insert(0,(x,y))
    sq= canvas.create_rectangle(x,y,x+SS,y+SS,fill=SC)
    snake.squares.insert(0,sq)
    if x == food.coordinates[0] and y == food.coordinates[1]:
        global score
        score +=1
        label.config(text="Score ={}".format(score))
        canvas.delete("food")
        food=Food()
    else :   
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]
    if CCol(snake):
        GOver()
    else :
        w.after(S,nextT,snake,food)
    

def CD(nd):
    global direction
    if nd=='left':
        if direction != 'right':
            direction= nd
    elif nd=='right':
        if direction != 'left':
            direction= nd
    elif nd=='up':
        if direction != 'down':
            direction= nd
    elif nd=='down':
        if direction != 'up':
            direction= nd


def CCol(snake):
    x, y=snake.coordinates[0]
    if x<0 or x>=W:
        return True
    if y<0 or y>=H:
        return True
    for BP in snake.coordinates[1:]:
        if x == BP[0] and y == BP[1]:
            return True
    return False
    

def GOver():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2,font=('consolas',70), text="GAME OVER", fill="red",tag="gameover")

w=Tk()
w.title("Snake game")
w.resizable(False, False)
score=0
direction='down'
label=Label(w,text="Score={}".format(score),font=('consolas',30))
label.pack()
canvas=Canvas(w,bg=BC,height=H,width=W)
canvas.pack()
w.update()
wW=w.winfo_width()
wH=w.winfo_height()
cW=w.winfo_screenwidth()
cH=w.winfo_screenheight()
x=int((cW/2)-(wW/2))
y=int((cH/2)-(wH/2))
w.geometry(f"{wW}x{wH}+{x}+{y}")
w.bind('<Left>',lambda event: CD('left'))
w.bind('<Right>',lambda event: CD('right'))
w.bind('<Up>',lambda event: CD('up'))
w.bind('<Down>',lambda event: CD('down'))
s=Snake()
f=Food()
nextT(s,f)

w.mainloop()