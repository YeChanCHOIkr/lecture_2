# arg_greet.py 참고!!!
def print_name(name):
    for i in range(len(name)):
        print(i+1, '번째는', name[i])

name_data = ['홍길동', '양만춘', '이순신', '안중근']
print(name_data)
print_name(name_data)