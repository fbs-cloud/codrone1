'''
def print_name(name):
    print("내 이름은 {0}입니다.".format(name))
print_name("파이썬")

def add(a=10, b=20):
    print(a+b)
add()
add(5,10)
'''
'''
def add(a=10, b=20):
    print(a+b)
add()
add(5,10)
'''
#람다 함수 = 익명함수

#print((lambda x : x*2)(5))
'''
a = lambda x, y : x+y
print(a(5,5))


a=[1,2,3,4,5]
print(list(filter(lambda s: s>3, a)))
'''

# 지역변수와 전역변수
'''
a = 10
def test():
    a=20
    print(a)
test()
print(a)

a = 10
def test():
    global a
    a=20
    print(a)
test()
print(a)

'''

def grade_info():
    score = int(input("점수를 입력하세요 "))
    if score >=90:
        print("성적은 A입니다.")
    elif score >= 80:
        print("성적은 B입니다.")
    elif score >= 70:
        print("성적은 C입니다.")
    elif score >= 60:
        print("성적은 D입니다.")
    else:
        print("성적은 F입니다.")
        
grade_info()
    

'''
def add(*a):
    return sum (a)
a = add (1,2,3,4,5)

print(a)
'''
