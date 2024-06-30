def fib(n):
    series=[0,1]
    for i in range(2,n):
        number=series[-1]+series[-2]
        series.append(number)
    return series[:n]
n=int(input())
print(fib(n))