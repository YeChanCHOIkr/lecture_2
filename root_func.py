def root_func(a,b,c):
    r1 = (-b + (b**2 - 4*a*c)**0.5)/(2*a)
    r2 = (-b - (b**2 - 4*a*c)**0.5)/(2*a)
    # r3 = a, b, c
    return r1, r2, # r3

# 한 번에 전체를 반환(return의 기본 묶음 기호는 소괄호!!)
root = root_func(1, 5, 6)
print(root)

# 각각 따로 반환
root1, root2 = root_func(1, 5, 6)
print('r1값은', root1)
print('r2값은', root2)