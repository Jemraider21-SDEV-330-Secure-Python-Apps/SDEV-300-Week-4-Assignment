# from Validation.validation import validate_input_not_blank
# from Validation.validation import validate_is_int
import Utils.Validation.validation as val
import numpy

ALL_MATRIXES: list[list] = []


def display_matrix(matrix: list[int]) -> str:
    output: str = ""
    index = 1
    for num in matrix:
        output = f'{output} {num}'
        if index == 3:
            output = output + "\n"
            index = 0
        index = index + 1
    return output


def display_all_matrix():
    print("Now displaying the matrixes")
    for matrix in range(1, 3):
        matrix_str = display_matrix(ALL_MATRIXES[matrix - 1])
        print(f'Matrix {matrix} \n {matrix_str}\n')


def generate_matrix(matrix_num: int) -> list[int]:
    matrix: list[int] = []
    for row_index in range(1, 4):
        for column_index in range(1, 4):
            prompt: str = f'Matrix {matrix_num} Row {row_index} Number {column_index}'
            matrix.append(val.validate_is_int(prompt))
    return matrix


def new_matrixes():
    ALL_MATRIXES.clear()
    for matrix_num in range(1, 3):
        ALL_MATRIXES.append(generate_matrix(matrix_num))
        print()


def display_matrix_result(prompt: str, matrix: list[int]):
    array: numpy.ndarray = []
    for row in range(1, 4):
        sub = []
        for column in range(1, 4):
            index = (row * column) - 1
            sub.append(matrix[index])
        array.append(sub)
    array = numpy.array(array)
    print(prompt)
    print(display_matrix(matrix))
    print(f'Transpose of the result:\n{array.transpose()}')
    print(f'Mean of rows:\n{numpy.mean(array, 0)}')
    print(f'Mean of columns:\n{numpy.mean(array, 1)}')


def matrix_menu():
    looper = True
    if ALL_MATRIXES.__len__ != 2:
        print("\nWe need to create some matrixes before we can continue\n")
        new_matrixes()
        display_all_matrix()

    while looper:
        print("\nMatrix Menu")
        print("1. Create new matrix")
        print("2. Display Current Matrixes")
        print("3. Matrix Addition")
        print("4. Matrix Subtraction")
        print("5. Matrix Multiplication")
        print("6. Element By Element Multiplication")
        print("7. Exit to Main Menu")
        user_input: int = val.validate_is_int("Matrix Menu Selection")
        match user_input:
            case 1:
                print()
                new_matrixes()
            case 2:
                display_all_matrix()
            case 3:
                result: list[int] = numpy.add(ALL_MATRIXES[0], ALL_MATRIXES[1])
                display_matrix_result("Adding the two matrixes:", result)
            case 4:
                result: list[int] = numpy.subtract(
                    ALL_MATRIXES[0], ALL_MATRIXES[1])
                display_matrix_result("Subtracting the two matrixes:", result)
            case 5:
                result: list[int] = numpy.matmul(
                    ALL_MATRIXES[0], ALL_MATRIXES[1])
                display_matrix_result("Multiplying the two matrixes:", result)
            case 7:
                looper = False
