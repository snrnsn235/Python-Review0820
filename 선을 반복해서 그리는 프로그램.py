'''
import turtle as t

angle = 120
t.bgcolor("black")
t.color("yellow")
t.speed(0)
for x in range(200):
    t.forward(x)
    t.left(angle)
'''
#태극 모양을 그리는프로그램
import turtle as t

t.bgcolor("black")
t.speed(0)

for x in range(200):
    if x % 4 == 0:
        t.color("blue")
    if x % 4 == 1:
        t.color("red")
    if x % 4 == 2:
        t.color("green")
    if x % 4 == 3:
        t.color("white")
    t.forward(x*2)
    t.left(90)
