def ispali(y):    
    
    for i in range(len(str(y))//2):
        size = len(str(y))
        print(size)
        i = 1
        first = 10 ** (size - 1)
        last = 10 ** i
        print(y)
        A = y // first
        B = y % last
        # print(124421 // 100000 , 124421 % 10) # first -->  = 10 ^ length - 1 and 10 ^ 1
        data = y - first * (A) - (B)
    
        y = data // last
        print(A,B,data//last)

        if A != B:
            return False
    else:
        return True
    
    

print(ispali(9999))




