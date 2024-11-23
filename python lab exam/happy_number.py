def isHappy(n):
        mem = set()
        while n != 1 and n not in mem:
            mem.add(n)
            x = 0
            while n > 0:
                temp = n % 10
                x += temp * temp
                n = n // 10
            n = x
        return n == 1

print(isHappy(19))