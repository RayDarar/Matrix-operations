# Matrix-operations
Simple matrix operations implemented in python. <br>Possible operations: summation, multiplication, finding determinant, finding inverse of a matrix

## Task list
- [x] Plan
- [x] Define class
- [x] Write tests
- [x] Implement logic

## Features
n - number of rows<br>
m - number of columns<br>
#### Four possible ways of creating matrix object:
- Matrix(): n = 1, m = 1
- Matrix(n, m)
- Matrix.generateFrom(data): data - two dimensional array
- Matrix.random(n, m)

#### Access data with index operator 
```python
matrix[n][m] = value
```

#### Supported operations
- Addition
- Multiplication

#### Useful methods
- determinant(): returns the determinant of a square matrix
- inverse(): returns the inverse matrix of a square matrix

## Licence
This repository is licensed under the MIT license - see the [LICENSE](LICENSE) for the details.
