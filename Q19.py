import re

class InvalidPanException(Exception):
    pass

def validate_pan(pan_number):
    pattern = r'^[A-Za-z]{5}[0-9]{4}[A-Za-z]{1}$'
    
    if not re.match(pattern, pan_number):
        raise InvalidPanException("Invalid PAN card Number")
    return "Valid PAN number"


def main():
    pan_number = input("Enter the PAN card number: ")
    
    try:

        result = validate_pan(pan_number)
        print(result)
    
    except InvalidPanException as e:
        print(e)
    
    finally:
        print("Pay Tax for Better India")

if __name__ == "__main__":
    main()
