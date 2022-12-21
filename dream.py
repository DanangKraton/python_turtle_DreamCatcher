import turtle as tur
import math

def Cir(t,size):
    for i in range(10):
        t.circle(size)
        size=size-2
    
def Circles(tur, size, repeat):
    for i in range(repeat):
        Cir(tur, size)
        tur.right(360/repeat)

def makeCircles(t,col, rad, numCol, numCir, dif):
    for i in range(numCol):
        t.color(col[i])
        Circles(t, rad - (i*dif), numCir)
    
    for i in range(4):
        t.left(90)
        t.color(col[0])
        t.circle(rad)

def whiteCir(t, rad):
    t.circle(rad, 180)
    t.color("white")
    t.circle(rad*2)

def renda(t,size):
    # for i in range(10):
    t.circle(size, 180)
        # size=size-4

def drawCircles(t,size,repeat):
  for i in range (int(repeat/2)):
    t.right(90-(360/repeat))
    renda(t,size)
    t.right(90 -(360/repeat))


bigCol = ["#FF087F", "#FF3898","#FF54A7", "#93F4F0", "#52EEE7", "#3C0D21"]
# smallCol = ["#FFB7A1", "#EFBC68", "#C2D7D0", "#5F9595"]
smallCol = ["#52EEE7", "#93F4F0", "#FF54A7", "#FF3898", "#FF087F"]

win = tur.Screen()
win.bgcolor("black")
win.title("DreamCatcher")

t = tur.Turtle()
t.speed(20)
t.color("black")
t.left(90)
t.forward(170)
t.right(90)

bigRad = 80
mediumRad = 30
smallRad = 20

rendaBig = 4*bigRad*math.sin(math.pi/216)
rendaMed = 4*mediumRad*math.sin(math.pi/72)
rendaSmall = 4*smallRad*math.sin(math.pi/72)


makeCircles(t, bigCol, bigRad, 5, 10, 12)

t.right(180)
whiteCir(t, bigRad)
t.color(bigCol[1])
drawCircles(t, rendaBig,216)
t.color("white")

t.right(90)
t.forward(50)
t.right(90)

t.color(smallCol[0])
t.circle(mediumRad, 180)

makeCircles(t, smallCol, mediumRad, 4, 8, 12)
t.right(180)
whiteCir(t, mediumRad)
t.color(smallCol[1])
drawCircles(t, rendaMed,72)
t.color("white")

t.right(90)
t.forward(30)
t.right(90)

t.color(smallCol[0])
t.circle(smallRad, 180)

makeCircles(t, smallCol, smallRad, 4, 8, 6)
t.right(180)
whiteCir(t, smallRad)
t.color(smallCol[1])
drawCircles(t, rendaSmall,72)
t.color("white")

t.circle(smallRad*2, 180)
t.right(90)
t.forward(30)
t.right(90)
t.circle(mediumRad*2, 180)
t.right(90)
t.forward(50)
t.right(90)
t.circle(bigRad*2, 90)
t.right(180)
t.forward(130)
t.right(90)
t.color(smallCol[0])
t.circle(smallRad, 180)
makeCircles(t, smallCol, smallRad, 4, 8, 6)
t.right(180)
whiteCir(t, smallRad)
t.color(smallCol[1])
drawCircles(t, rendaSmall,72)
t.color("white")

t.circle(smallRad*2, 180)
t.right(90)
t.forward(130)
t.circle(bigRad*2, 180)
t.forward(130)
t.right(90)
t.color(smallCol[1])
t.circle(smallRad, 180)
makeCircles(t, smallCol, smallRad, 4, 8, 6)
t.right(180)
whiteCir(t, smallRad)
t.color(smallCol[1])
drawCircles(t, rendaSmall, 72)
t.color("white")

tur.done()