#import turtle
#import turtle as t
#360/각도 예) 정삼각형은 360/3 = 120
'''
#정사각형 그리기
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
print()
'''
'''
#정삼각형 그리기
t.forward(100)
t.right(120)
t.forward(100)
t.right(120)
t.forward(100)
t.right(120)
'''
'''

#정오각형 그리기
t.color("black","white") #선색, 면색 지정하기
t.begin_fill()#채우기 시작하기
t.shape("turtle")#거북이 모양바꾸기
t.speed(1)#거북이 속도 조적하기
'''
'''
t.forward(100)#앞으로 나아가기
t.right(72)#오른쪽 방향을 각도만큼 회전하기
t.forward(100)
t.right(72)
t.forward(100)
t.right(72)
t.forward(100)
t.right(72)
t.forward(100)
t.right(72)
t.end_fill()#채우기 종료
t.clear()#거북이 지우기 

for i in range(0, 5, 1):
    t.forward(100)
    t.right(72)
    t.end_fill()
'''
'''
for i in range(0, 5, 1):
    t.forward(100)
t.right(72)
t.end_fill()
'''
'''
for i in [0,1,2,3,4]:
    t.forward(100)
    t.right(72)
    t.end_fill()
'''
'''
from turtle import*
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()'''

#for문을 이용해서 1부터 n까지의 합을 구하는 튜토리
i, hap = 0, 0
num=0
num=int(input("값 입력 : "))
for i in range(1, num+1, 1):
    hap=hap+i
print("1에서 %d까지 합 : %d" %(num, hap))    
    
i=1, 
num=0
while i<num+1:
    hap=hap+i
    i=i+1
    
print("1에서 %d까지 합 : %d" %(num,hap))



