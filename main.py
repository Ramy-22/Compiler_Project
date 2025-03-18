from identifier import is_valid_identifier

if __name__ == '__main__':
    user_input = input("Enter an identifier to check its validity: ")
    if is_valid_identifier(user_input):
        print(f"'{user_input}' is a valid identifier.")
    else:
        print(f"'{user_input}' is not a valid identifier")