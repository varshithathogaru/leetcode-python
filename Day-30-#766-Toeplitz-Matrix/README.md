# LeetCode #766 - Toeplitz Matrix

## 🧩 Problem

Given an m x n matrix, return `True` if the matrix is a Toeplitz
matrix.

A matrix is Toeplitz if every diagonal from top-left to bottom-right
contains the same elements.

## 💡 Approach

I used a direct diagonal comparison approach.

For every element `matrix[i][j]`, I compare it with its upper-left
diagonal neighbor:

`matrix[i-1][j-1]`

If they are different, the matrix is not Toeplitz, so I immediately
return `False`.

If all valid diagonal pairs match, I return `True`.

## 🧠 Python Solution

```python
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[i])):
                if matrix[i][j] != matrix[i - 1][j - 1]:
                    return False

        return True
