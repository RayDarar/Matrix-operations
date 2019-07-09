# Matrix class
# n (int) - amount of rows
# m (int) - amount of columns

import random as rnd


class Matrix(object):
    def __init__(self, n=1, m=1, data=list()):
        if n >= 1 and m >= 1:
            self.n = n
            self.m = m
            if len(data) == 0:
                self.data = [[0 for i in range(m)] for i in range(n)]
            else:
                self.data = data
        else:
            raise Exception("Incorrect input")

    def __getitem__(self, i):
        return self.data[i]

    @staticmethod
    def generateFrom(data=list()):
        if isinstance(data, type([[]])):
            return Matrix(len(data), len(data[0]), data)
        raise Exception()

    @staticmethod
    def random(n=1, m=1):
        result = Matrix(n, m)
        for i in range(n):
            for j in range(m):
                result[i][j] = rnd.randint(0, 9)
        return result

    def sum(self, other):
        if isinstance(other, type(self)):
            if self.n * self.m == other.n * other.m:
                result = Matrix(self.n, self.m)

                for i in range(self.n):
                    for j in range(self.m):
                        result[i][j] = self[i][j] + other[i][j]

                return result
        raise Exception("")

    def __add__(self, other):
        return self.sum(other)

    def calcOne(self, first, second):
        result = 0
        for i in range(len(first)):
            result += first[i] * second[i]
        return result

    def transpose(self):
        result = Matrix(self.m, self.n)

        for i in range(self.n - 1, -1, -1):
            temp = self[i]
            for j in range(self.m):
                result[j][i] = temp[j]
        return result

    def mul(self, other):
        if isinstance(other, type(0)) or isinstance(other, type(1.0)):
            result = Matrix(self.n, self.m)

            for i in range(self.n):
                for j in range(self.m):
                    result[i][j] = self[i][j] * other

            return result
        elif isinstance(other, type(self)):
            if self.n == other.m and self.m == other.n:
                data = [[0 for i in range(self.n)] for i in range(self.n)]

                temp = other.transpose()

                for i in range(self.n):
                    for j in range(self.n):
                        data[i][j] = self.calcOne(self[i], temp[j])

                return Matrix.generateFrom(data)

        raise Exception("")

    def __mul__(self, other):
        return self.mul(other)

    def __rmul__(self, other):
        return self.mul(other)

    pass
