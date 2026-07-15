"""
Project Name: Matrix Calculator

Description:
This program allows the user to perform basic matrix operations:
- Addition
- Subtraction
- Multiplication
- Determinant calculation (recursive)

The matrices are stored as lists of lists in Python, and all operations
are implemented using loops and functions. Users input the dimensions
and elements of the matrices interactively.

Concepts Used:
- Lists (nested lists for matrices)
- Loops (for loops)
- Functions
- Conditional statements (if, elif, else)
- User input using input()
- Basic recursion for determinant calculation
- Input validation
"""

# Function to input a matrix
def input_matrix(rows, cols):
    print(f"Enter elements of the matrix ({rows}x{cols}):")
    matrix = []

    for i in range(rows):
        row = []
        for j in range(cols):
            val = int(input(f"Element [{i+1},{j+1}]: "))
            row.append(val)
        matrix.append(row)

    return matrix

# Function to display a matrix
def display_matrix(matrix):
    print("Matrix:")
    for row in matrix:
        for val in row:
            print(val, end="\t")
        print()

# Matrix addition
def add_matrices(A, B):
    rows, cols = len(A), len(A[0])
    result = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(A[i][j] + B[i][j])
        result.append(row)
    return result

# Matrix subtraction
def subtract_matrices(A, B):
    rows, cols = len(A), len(A[0])
    result = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(A[i][j] - B[i][j])
        result.append(row)
    return result

# Matrix multiplication
def multiply_matrices(A, B):
    r1, c1 = len(A), len(A[0])
    r2, c2 = len(B), len(B[0])
    result = [[0 for _ in range(c2)] for _ in range(r1)] # 2X2 size matrix >> [[0,0][0,0]]
    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
                result[i][j] += A[i][k] * B[k][j]
    return result

# Determinant calculation (recursive)
def determinant(matrix):
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    if n == 2:
        return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]

    det = 0
    for p in range(n):
        # Build submatrix
        submatrix = []
        for i in range(1, n):
            row = []
            for j in range(n):
                if j != p:
                    row.append(matrix[i][j])
            submatrix.append(row)
        det += matrix[0][p] * determinant(submatrix) * (1 if p % 2 == 0 else -1)
    return det

# Main program
def main():
    while True:
        print("\n=== Matrix Calculator ===")
        print("1. Add Matrices")
        print("2. Subtract Matrices")
        print("3. Multiply Matrices")
        print("4. Determinant")
        print("5. Exit")
        choice = int(input("Enter choice: "))

        if choice in [1, 2, 3]:
            r1 = int(input("Enter rows for Matrix A: "))
            c1 = int(input("Enter columns for Matrix A: "))
            r2 = int(input("Enter rows for Matrix B: "))
            c2 = int(input("Enter columns for Matrix B: "))
            
            if choice in [1, 2] and (r1 != r2 or c1 != c2):
                print("Error: Matrices must have the same dimensions for addition/subtraction.")
                continue
            if choice == 3 and c1 != r2:
                print("Error: Columns of A must equal rows of B for multiplication.")
                continue

            A = input_matrix(r1, c1)
            B = input_matrix(r2, c2)

            if choice == 1:
                result = add_matrices(A, B)
                print("Result of Addition:")
                display_matrix(result)
            elif choice == 2:
                result = subtract_matrices(A, B)
                print("Result of Subtraction:")
                display_matrix(result)
            elif choice == 3:
                result = multiply_matrices(A, B)
                print("Result of Multiplication:")
                display_matrix(result)

        elif choice == 4:
            n = int(input("Enter size of square matrix (n x n): "))
            matrix = input_matrix(n, n)
            det = determinant(matrix)
            print("Determinant:", det)

        elif choice == 5:
            print("Exiting Matrix Calculator...")
            break
        else:
            print("Invalid choice!")

main()