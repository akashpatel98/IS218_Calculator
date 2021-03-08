def check(func):
    def inside(a, b):
        if b == 0:
            print('not dividable by 0')
            return
        func(a, b)
    return inside
