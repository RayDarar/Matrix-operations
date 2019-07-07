# Matrix class
# n (int) - amount of rows
# m (int) - amount of columns


class Matrix(object):
    def __init__(self, n: int, m: int):
        if n >= 0 and m >= 0:
            self.n = n
            self.m = m
        else:
            raise Exception("Incorrect input")
    pass
