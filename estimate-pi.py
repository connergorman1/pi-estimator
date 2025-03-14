import random
import math
def gcd(a: int, b: int) -> int:
    if b == 0:
        return a
    r = a % b
    
    return gcd(b, r)

def main(_range):
    count = 0
    for i in range(_range):
        a = random.randint(1,_range)
        b = random.randint(1,_range)
        if a > b:
            _gcd = gcd(a,b)
        else:
            _gcd = gcd(b,a)
        if _gcd == 1:
            count+=1
    mu = float(count) / float(_range)
    est = math.sqrt(6 / mu)
    print(f"# samples: {_range}, Pi:{est}")


if __name__ == "__main__":
    for i in [10, 100, 1000, 100000, 10000000]:
        main(i)
