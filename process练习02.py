"""
练习02：
创建一个子进程，子进程传入两个整数
求着两个整数之间的所有质数之和

1   1000---->打印出1~1000的质数之和

质数：只能被1和它本身整除>1的整数
"""
from multiprocessing import Process


# def is_prime():

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True


def num(num01, num02):
    count = 0
    for i in range(num01, num02):
        if is_prime(i):
            count += i
    print(count)


p = Process(target=num, args=(1, 1000))

p.start()
