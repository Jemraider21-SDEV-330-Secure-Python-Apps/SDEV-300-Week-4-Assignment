# Prompt and validate phone number
import re
import Utils.Matrix.matrix as mat
import Utils.Validation.validation as val


PHONENUMBER: re.Pattern = re.compile(r'^(\d{3})\D*(\d{3})\D*(\d{4})\D*(\d*)$')
ZIPCODE: re.Pattern = re.compile(r'^\d{5}(?:[-\s]\d{4})?$')


def validate_entry(pattern: re.Pattern, input_name: str, additional_info: str, input_length: int) -> None:
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
    print("\nMain Menu")
    user_input: int = 0
    looper: bool = True
    while looper:
        print("1. Validate Phone Number")
        print("2. Validate Zip Code")
        print("3. Matrix Operations")
        print("4. Exit")
        user_input: int = val.validate_is_int("Main Menu Option")
        if user_input in range(1, 5):
            looper = False
        else:
            print("Choice not valid. Please try again")
    return user_input


def main():
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
    print("\nEnd of program. Goodbye!")


main()
