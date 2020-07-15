def div(a = 1, b = 2):
    return a / b

print('div() =', div()) # 인자가 없을 경우 div(1, 2)
print('div(4) =', div(4)) # div(4, 2)
print('div(6, 3) =', div(6, 3))

print('div(b = 6, a = 3) =', div(b = 6, a = 3)) # 키워드 인자로 전달