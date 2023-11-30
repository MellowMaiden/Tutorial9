import math
import random
def f(x):
    return sum([x**n/math.factorial(n) for n in range(11)])
def g(x):
    if x>0:
        return 1
    elif x<0:
        return -1
    else:
        return 0
def r():
    return random.randint(-100,100)
for loop in range (1,4):
    x=r()
    print(f"#{x}")
    fx=f(x)
    print(f"for this value of x, f(x) will be {fx:.1f}")
    gx=g(x)
    print(f"for this value of x, g(x) will be {gx}")
    fgfx=f(g(fx))
    print(f"for this value of x, f(g(f(x))) will be {fgfx:.1f}")
    print("#"*40)
