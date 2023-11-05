def grey_code(num, length):
    if num < 0:
        return "not convertible"
    elif num == 0:
        return 0
    res = []
    while num > 0:
        red = num % 2
        res.append(str(red))
        num = num // 2
        
    res.reverse()
    
    out = res[0]
    l = 0
    one = "1"
    zero = "0"
    for bit in res[1:]:
        if res[l] != bit:
            out += one
        else:
            out += zero
        l += 1
        
    if len(out) < length:
        out = "0" * (length - len(out)) + out
        
        
    return out
print(grey_code(12,16))



