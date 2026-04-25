import numpy as np


def input_matrix(name):
    rows = int(input(f"Enter number of rows for {name}: "))
    cols = int(input(f"Enter number of columns for {name}: "))
    print(f"Enter elements for {name} row-wise:")
    elements = []
    for i in range(rows):
        row = list(map(float, input(f"Row {i+1}: ").split()))
        elements.append(row)
    return np.array(elements)


def display_menu():
    print("\nMatrix Operations Tool")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Transpose")
    print("5. Determinant")
    print("6. Exit")


while True:
    display_menu()
    choice = input("Enter your choice: ")

    if choice == '1':
        A = input_matrix("Matrix A")
        B = input_matrix("Matrix B")
        if A.shape == B.shape:
            result = A + B
            print("Result (A + B):\n", result)
        else:
            print("Error: Matrices must have same dimensions.")

    elif choice == '2':
        A = input_matrix("Matrix A")
        B = input_matrix("Matrix B")
        if A.shape == B.shape:
            result = A - B
            print("Result (A - B):\n", result)
        else:
            print("Error: Matrices must have same dimensions.")

    elif choice == '3':
        A = input_matrix("Matrix A")
        B = input_matrix("Matrix B")
        if A.shape[1] == B.shape[0]:
            result = np.dot(A, B)
            print("Result (A x B):\n", result)
        else:
            print("Error: Columns of A must equal rows of B.")

    elif choice == '4':
        A = input_matrix("Matrix")
        result = A.T
        print("Transpose:\n", result)

    elif choice == '5':
        A = input_matrix("Matrix")
        if A.shape[0] == A.shape[1]:
            result = np.linalg.det(A)
            print("Determinant:\n", result)
        else:
            print("Error: Matrix must be square.")

    elif choice == '6':
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Try again.")
