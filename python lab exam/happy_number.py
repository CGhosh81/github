def ishappy(n):
    mem = set()
    while n != 1:
        if n in mem:
            return False
        mem.add(n)
        n = sum(int(i) ** 2 for i in str(n))
    return True

print(ishappy(19))  # Output: True
