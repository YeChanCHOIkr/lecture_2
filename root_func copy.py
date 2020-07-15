def root_func(a = 1, b = 2, c):
    r1 = (-b + (b**2 - 4*a*c)**0.5)/(2*a)
    r2 = (-b - (b**2 - 4*a*c)**0.5)/(2*a)
    return r1, r2

#SyntaxError: non-default argument follows default argumentroot = root_func(8)
print(root)

#SyntaxError: invalid syntax
root1, root2 = root_func(,, 8)
print('r1값은', root1)
print('r2값은', root2)