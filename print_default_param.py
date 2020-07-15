def print_star(n=1): #매개변수 n값 = 디폴트 1
    for _ in range(n):
        print('******************************************')

print_star() #인자가 없더라도 에러 없이 수행됨

print('인자값으로 위치인자 3')
print_star(3)

print('인자값으로 키워드인자 4')
print_star(n=4)