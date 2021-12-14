#반복문을 이용한 구구단 출력
'''
#2단 출력
for y in range(1,10,1):
    print('2x{}={}'.format(y, 2*y))
'''
'''
#구구단 출력
for x in range(2,10,1): #2에서 9까지 1씩 증가한다.2단 ,3단,4단...9단
    for y in range(1,10,1): #1~9까지 
        print('{}x{}={}'.format(x,y,x*y))
'''
'''
#구구단 출력 단마다 띄어쓰기
for x in range(2,10,1): #2에서 9까지 1씩 증가한다.2단 ,3단,4단...9단
    for y in range(1,10,1): #1~9까지 
        print('{}x{}={}'.format(x,y,x*y))
    print('')
'''
'''
#구구단 출력, 단마다 가로로 출력하기
for x in range(2,10,1): #2에서 9까지 1씩 증가한다.2단 ,3단,4단...9단
    for y in range(1,10,1): #1~9까지 
        print('{}x{}={},'.format(x,y,x*y), end=" ")
    print()
'''
'''
#구구단 출력을 while문으로 바꾸기
#2단
i=1
while i<10:
    print('2x{}={}'.format(i, 2*i))
    i=i+1
 '''
    
#while문을 이용
#구구단 출력하기
x = 2 #초기값1
while x<10: #조건식("끝값")1
    y=1#초기값2
    while y<10:#조건식("끝값")2
        print('{}x{}={}, '.format(x,y,x*y), end=" ")
        y=y+1#증감식2
    print()
    x=x+1#증감식1



























