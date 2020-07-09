
def fibo(n): #iterative
    if n == 0:
        return 0
    a = 0
    b = 1
    for i in range(n):
        c = a+b # 1 , 1
        a = b
        b = c
    return c




def power(x,n): #iterative
    result = 1
    for i in range(n):
        result *=x
    return result

def power(x,n): #recursive
    " x^n = x * x^n-1"
    if n == 0:
        return 1
    return x * power(x, n-1)


if __name__ == "__main__":
    print(fibo(5))
    print(power(2,4))
    print(power(2,4))