def arg_kwarg_param2(*args, **kwargs):
    print(len(args))
    print(len(kwargs))
    print(args, kwargs)
    return args, kwargs

result1, result2 = arg_kwarg_param2(10, 20, a=30, b=40)
print(result1)
print(result2)