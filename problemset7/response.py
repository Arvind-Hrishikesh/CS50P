from validator_collection import validators, checkers, errors

value=input("Email: ")
try:
    validators.email(value, allow_empty=False)
except (errors.InvalidEmailError,errors.EmptyValueError,errors.CannotCoerceError):
    print("Invalid")
else:
    print("Valid")