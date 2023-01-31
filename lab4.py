# Prompt and validate phone number
import re
from Validation.validation import validate_input_not_blank

PHONENUMBER: re.Pattern = re.compile(r'^(\d{3})\D*(\d{3})\D*(\d{4})\D*(\d*)$')
ZIPCODE: re.Pattern = re.compile(r'^\d{5}(?:[-\s]\d{4})?$')


def validate_entry(pattern: re.Pattern, input_name: str, additional_info: str, input_length: int) -> None:
    print(f'Validating {input_name}')
    looper: bool = True
    while looper:
        user_input = validate_input_not_blank(input_name, additional_info)
        match = pattern.search(user_input)
        if match is not None and len(match.group()) == input_length:
            print(f'This is a valid {input_name} - {user_input}')
            looper = False
        else:
            print(
                f'The following {input_name} is not valid. Please try again: {user_input}')


def main():
    validate_entry(PHONENUMBER, "Phone Number", "xxx-xxx-xxxx", 12)
    print()
    validate_entry(ZIPCODE, "Zip Code", "xxxxx-xxxx", 10)


main()
