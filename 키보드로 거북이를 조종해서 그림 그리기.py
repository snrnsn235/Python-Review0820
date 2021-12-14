import turtle as t

def turn_right(): #오른쪽으로 이동하는 함수
    t.setheading(0) #.tseth(0)으로 입력해도 됨
    t.forward(10) #t.fd(10)으로 입력해도 됨

def turn_up(): #위쪽으로 이동하는 함수
    t.setheading(90) 
    t.forward(10) 
    
def turn_left(): #왼쪽으로 이동하는 함수
    t.setheading(180) 
    t.forward(10) 

def turn_down(): #오른쪽으로 이동하는 함수
    t.setheading(270)
    t.forward(10) 

def blank(): #화면을 지우는 함수
    t.clear() 

t.shape("turtle")
t.color("green")
t.bgcolor("black")
t.speed(0)
t.onkeypress(turn_right,"Right") # ->를 누르면 turn_right함수를 실행
t.onkeypress(turn_up,"Up") # 를 누르면 turn_up함수를 실행
t.onkeypress(turn_left,"Left") #->를 누르면 turn_left함수를 실행
t.onkeypress(turn_down,"Down") # 를 누르면 turn_down함수를 실행
t.onkeypress(blank,"Escape") # 를 누르면 blank 함수를 실행
t.listen() #거북이 그래픽 창이 키보드 입력을 받
