# Test module
# Run any test you want
# Test list:
# 1) Create objects with different inputs
# 2) Accessing any matrix cell, writing & reading
# 3) Inputing matrix data by console
# 4) Randoming values in matrix
# 5) Summation
# 6) Multiplication (by constant or matrix)
# 7) Finding matrix determinant
# 8) Finding inverse of matrix

from matrix import Matrix


def test_createObjects():
    try:
        correct = Matrix(1, 1)
        print("Correct object created")

        wrong = Matrix(0, 0)

        print("Test failed")
        return
    except:
        print("Wrong object created")

    print("Test passed")
    pass

def test_accessData():
    try:
        temp = Matrix()
        print("Data 0 | 0:", temp[0][0])
        temp[0][0] = 100
        print("New Data 0 | 0:", temp[0][0])
        print("Test passed")
    except:
        print("Test failed")
    pass


def test_inputData():
    try:
        data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        temp = Matrix.generateFrom(data)
        if temp[0][0] == 1 and temp[2][2] == 9:
            print("Test passed")
        else:
            raise Exception("")
    except Exception as e:
        print("Test failed")
        print(e)
    pass


def test_randomizeData():
    try:
        temp1 = Matrix.random(3, 3)
        temp2 = Matrix.random(3, 3)
        if (temp1[0][0] != temp2[0][0]):
            print("Test passed")
        else:
            raise Exception("")
    except:
        print("Test failed")
    pass


def test_summation():
    try:
        temp1 = Matrix.generateFrom([[1]])
        temp2 = Matrix.generateFrom([[2]])
        temp3 = temp1 + temp2

        if temp3[0][0] == 3:
            print("Test passed")
        else:
            raise Exception("")
    except:
        print("Test failed")
    pass


def test_multiplication():
    try:
        temp1 = Matrix.generateFrom([[1, 2], [2, 1], [2, 2]])
        temp2 = Matrix.generateFrom([[3, 3, 3], [3, 3, 3]])

        temp2 = (1 / 3) * temp2

        if temp2[0][0] != 1:
            raise Exception("")

        temp3 = temp1 * temp2

        if (temp3[0][0] != 3):
            raise Exception("")
        print("Test passed")
    except:
        print("Test failed")
    pass


def test_determinant():
    pass


def test_inverse():
    pass

test_summation()