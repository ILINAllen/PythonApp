# 例4：
# 说明：yield from iterable本质上等于for item in iterable: yield item的缩写版

def fab3(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        print('is ',b)
        a, b = b, a + b
        n = n + 1

def f_wrapper1(f):
    for g in f:
        yield g


wrap = f_wrapper1(fab3(5))
for i in wrap:
    print(i, end=' ')

print('\n使用yield from代替for循环')


def f_wrapper2(f):
    yield from f  # 注意此处必须是一个可生成对象


wrap = f_wrapper2(fab3(5))
for i in wrap:
    print(i, end=' ')
print('\n---------------------')

print('yield from包含多个子程序')


def g(x):
    yield from range(x, 0, -1)
    yield from range(x)


print(list(g(5)))
for g in g(6):
    print(g, end=',')

print('\n---------------------')
# 注意红色部分就是替代的部分，yield from iterable本质上等于for item in iterable: yield item的缩写版