"""Operations for working with matrixes
"""
import numpy
import Utils.Validation.validation as val
import Utils.Matrix.matrixutils as matutils

ALL_MATRIXES: list[list] = []
MAX_MATRIX = 2


def new_matrixes():
    """Clear out the list of matixes and add new matrixes
    """
    ALL_MATRIXES.clear()
    for matrix_num in range(1, MAX_MATRIX + 1):
        matrix: list[int] = matutils.generate_matrix(matrix_num)
        ALL_MATRIXES.append(matrix)
        print()


def display_matrix_result(prompt: str, matrix: list[int]):
    """Expand a one dimensional array matrix and perform some
    matrix based statistic calculations for it

    Args:
        prompt (str): Operational prompt
            Ex: "Matrix Multiplications"
        matrix (list[int]): One dimensional array matrix
            Ex: [1, 2, 3, ...]
    """
    expanded: list[list] = matutils.expand_matrix(matrix)
    print(prompt)
    print(matutils.display_matrix(matrix))
    print(f'Transpose of the result:\n{numpy.transpose(expanded)}')
    print(f'Mean of rows:\n{numpy.mean(expanded, 0)}')
    print(f'Mean of columns:\n{numpy.mean(expanded, 1)}')


def menu_display():
    """Print out menu options for working with a matrix
    """
    print("\nMatrix Menu")
    print("1. Create new matrix")
    print("2. Display Current Matrixes")
    print("3. Matrix Addition")
    print("4. Matrix Subtraction")
    print("5. Matrix Multiplication")
    print("6. Element By Element Multiplication")
    print("7. Exit to Main Menu")


def menu_actions(user_input: int) -> bool:
    """Perform a matrix action based on user input

    Args:
        user_input (int): The menu selection from the user

    Returns:
        bool: Whether to break the main menu loop for matrixes
    """
    looper = True
    match user_input:
        case 1:
            print()
            new_matrixes()
        case 2:
            matutils.display_all_matrix(ALL_MATRIXES)
        case 3:
            result: list[int] = numpy.add(ALL_MATRIXES[0], ALL_MATRIXES[1])
            display_matrix_result("Adding the two matrixes:", result)
        case 4:
            result: list[int] = numpy.subtract(
                ALL_MATRIXES[0], ALL_MATRIXES[1])
            display_matrix_result("Subtracting the two matrixes:", result)
        case 5:
            result: list[int] = numpy.multiply(
                ALL_MATRIXES[0], ALL_MATRIXES[1])
            display_matrix_result("Multiplying the two matrixes:", result)
        case 6:
            result: list[int] = []
            for index in range(9):
                val1 = ALL_MATRIXES[0][index]
                val2 = ALL_MATRIXES[1][index]
                result.append(val1 * val2)
            display_matrix_result(
                "Multiplying element by element:", result)
        case 7:
            looper = False
        case _:
            print("Invalid menu input. Please try again")
    return looper


def matrix_menu():
    """Main menu for handling functions with matixes
    """
    looper = True

    # For testing to avoid having to create matixes
    ALL_MATRIXES.append([1, 2, 4, 4, 2, 1, 3, 8, 9])
    ALL_MATRIXES.append([3, 2, 1, 7, 2, 5, 5, 2, 1])

    # Use for official code
    # if len(ALL_MATRIXES) != 2:
    #     print("\nWe need to create some matrixes before we can continue\n")
    #     new_matrixes()
    #     matutils.display_all_matrix()

    while looper:
        menu_display()
        user_input: int = val.validate_is_int("Matrix Menu Selection")
        looper = menu_actions(user_input)
