

def is_valid(s):
    # Requirement 1 & 2: length between 2 and 6
    if len(s) < 2 or len(s) > 6:
        return False

    # Requirement 3: must start with at least two letters
    if not s[0].isalpha() or not s[1].isalpha():
        return False

    # Requirement 4: only letters and numbers allowed
    if not s.isalnum():
        return False

    # Requirement 5: numbers must be at the end and not start with 0
    number_started = False
    for char in s:
        if char.isdigit():
            if not number_started:
                # First number cannot be '0'
                if char == "0":
                    return False
                number_started = True
        else:
            # If a letter appears after a number, it's invalid
            if number_started:
                return False

    return True


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


main()
