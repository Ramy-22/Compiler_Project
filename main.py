from identifier_scanner import scan_identifiers

if __name__ == '__main__':
    input_string = input("Enter code as a string to scan for valid identifiers: ")
    identifiers = scan_identifiers(input_string)
    print(f"valid identifiers: {identifiers}")