"""Main menu for the program. Prompt for input to:
    * Validate phone number
    * Validate zip code
    * Perform matix operations
"""

import re
import Utils.Matrix.matrix as mat
import Utils.Validation.validation as val


PHONENUMBER: re.Pattern = re.compile(r'^(\d{3})\D*(\d{3})\D*(\d{4})\D*(\d*)$')
ZIPCODE: re.Pattern = re.compile(r'^\d{5}(?:[-\s]\d{4})?$')


def validate_entry(pattern: re.Pattern, input_name: str,
                   additional_info: str, input_length: int) -> None:
    """Prompt for user input and validate it against a regex pattern

    Args:
        pattern (re.Pattern): regex pattern to validate against
        input_name (str): Name for input
            ex: "Phone Number"
        additional_info (str): any additional information for the input name
            Ex: (kgs)
        input_length (int): Expected length of the user input
            ex: num == {10}
    """
    print(f'Validating {input_name}')
    looper: bool = True
    while looper:
        user_input = val.validate_input_not_blank(
            input_name, additional_info)
        match = pattern.search(user_input)
        if match is not None and len(match.group()) == input_length:
            print(f'This is a valid {input_name} - {user_input}')
            looper = False
        else:
            print(
                f'The following {input_name} is not valid. Please try again: {user_input}')


def main_menu() -> int:
    """Display main menu selections and prompt for input

    Returns:
        int: user input for menu selection
    """
    print("\nMain Menu")
    print("1. Validate Phone Number")
    print("2. Validate Zip Code")
    print("3. Matrix Operations")
    print("4. Exit")
    user_input: int = val.validate_is_int("Main Menu Option")
    return user_input


def main():
    """Display the main menu and perform action
    """
    looper: bool = True
    while looper:
        user_input: int = main_menu()
        match user_input:
            case 1:
                validate_entry(PHONENUMBER, "Phone Number", "xxx-xxx-xxxx", 12)
            case 2:
                validate_entry(ZIPCODE, "Zip Code", "xxxxx-xxxx", 10)
            case 3:
                mat.matrix_menu()
            case 4:
                looper = False
            case _:
                print("Choice not valid. Please try again")
    print("\nEnd of program. Goodbye!")


if __name__ == "__main__":
    main()
