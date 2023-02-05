"""Helper functions for working with matrixes
"""
import Utils.Validation.validation as val


def display_matrix(matrix: list[int]) -> str:
    """Prints the matrix out to the console in the correct format

    Args:
        matrix (list[int]): One dimensional matrix array
        Ex: [1, 2, 3, ...]

    Returns:
        str: String representation of the matrix in grid form
    """
    output: str = ""
    index = 1
    for num in matrix:
        output = f'{output} {num}'
        if index == 3:
            output = output + "\n"
            index = 0
        index = index + 1
    return output


def display_all_matrix(matrixes: list[list]):
    """Taking a list of matrixes, display them all

    Args:
        matrixes (list[list[int]]): Array of matrixes
    """
    print("Now displaying the matrixes")
    counter = 1
    for matrix in matrixes:
        matrix_str = display_matrix(matrix)
        print(f'Matrix {counter} \n {matrix_str}\n')
        counter = counter + 1


def flatten_matrix(matrix: list[list]) -> list[int]:
    """Taking a multidimensional array matrix, convert it into a one dimensional array matrix

    Args:
        matrix (list[list]): the multidimensional array matrix
        Ex: [[1,2], [3,4], ...]

    Returns:
        list[int]: The one dimensional array matrix
        Ex: [1, 2, 3, ...]
    """
    flat: list[int] = []
    for row in matrix:
        for column in row:
            flat.append(column)
    return flat


def expand_matrix(matrix: list[int]) -> list[list]:
    """Taking a flattened  matrix, convert it into a multidimensional array matrix

    Args:
        matrix (list[int]): The one dimensional array matrix to expand
        Ex: [1, 2, 3, ...]

    Returns:
        list[list]: the multidimensional array matrix
        Ex: [[1,2], [3,4], ...]
    """
    expand: list[list] = []
    for row in range(1, 4):
        sub: list[int] = []
        for column in range(1, 4):
            index: int = (row * column) - 1
            sub.append(matrix[index])
        expand.append(sub)
    return expand


def generate_matrix(matrix_num: int) -> list[int]:
    """Generate a one dimensional array matrix based on user input

    Args:
        matrix_num (int): Counter for matrix
        Ex: Matrix {1}

    Returns:
        list[int]: The newly created matrix
    """
    matrix: list[int] = []
    for row_index in range(1, 4):
        for column_index in range(1, 4):
            prompt: str = f'Matrix {matrix_num} Row {row_index} Number {column_index}'
            matrix.append(val.validate_is_int(prompt))
    return matrix
