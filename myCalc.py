# 함수
def add_func(n1,n2):
    return n1+n2

def sub_func(n1,n2):
    return n1-n2

def mul_func(n1,n2):
    return n1*n2


def div_func(n1,n2):
    return n1/n2

def ss_func(n1,n2):
    return n1**n2

# 전역
num1,num2,result = 100,200,0

# 메인
result = add_func(num1,num2)
print(num1,"+",num2,"=",result)

result = sub_func(num1,num2)
print(num1,"-",num2,"=",result)

result = mul_func(num1,num2)
print(num1,"*",num2,"=",result)

result = div_func(num1,num2)
print(num1,"/",num2,"=",result)


result = ss_func(num1,num2)
print(num1,"**",num2,"=",result)
