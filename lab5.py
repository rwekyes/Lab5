# Part 1: Conditional Validation of IP Addresses
# Task 1: Validating IP Address Parts

def is_valid_part(part):
    if not part.isdigit(): # isinstance wasn't working great, found this instead
        return False
    if int(part[0]) == 0 and len(part) > 1:
        return False
    return 0 <= int(part) < 256

# Task 2: Validating the Full IP Address

def is_valid_ip(ip):
    split_ip = ip.split('.')
    if len(split_ip) != 4:
        return False
    for part in split_ip:
        if not is_valid_part(part):
            return False
    return True

# Part 2: Recursion and Number Conversion
# Task 1: Convert Decimal to Binary (Recursion)

def decimal_to_binary(n):
    if n < 2:
        return str(n)
    return decimal_to_binary(n//2) + str(n % 2)

# Task 2: Convert Binary to Decimal (Recursion)

def binary_to_decimal(n):
    if n == "":
        return 0
    return int(n[0]) * 2 ** (len(n)-1) + binary_to_decimal(n[1:])

# Part 3: (BONUS+10pts) Combining Recursion and Conditionals (Optional)
# Task 1: IP Address and Binary Conversion
# Task 2: Bonus-Bonus (BONUS+5pt) Exercise (Extra Optional)

import re # Got fancy with regex

def is_valid_bin_part(part):
    if len(part) != 8:
        return False
    return not bool(re.search(r"[^01]", part))

def is_valid_binary(ip):
    split_ip = ip.split('.')
    if len(split_ip) != 4:
        return False
    for part in split_ip:
        if not is_valid_bin_part(part):
            return False
    return True

def leading_zeros(n):
    if len(n) < 9:
        n = "0" + n
        return leading_zeros(n)
    else:
        return n

def ip_to_binary(ip):
    binary = ""
    if is_valid_ip(ip):
        split_ip = ip.split('.')
        if len(split_ip) != 4:
            return "Error - Invalid IP"
        for part in split_ip:
            binary += leading_zeros(decimal_to_binary(int(part)) + ".")
        return binary[:-1]
    else:
        return "Error - Invalid IP"

def binary_to_ip(binary):
    decimal = ""
    split_bin = binary.split('.')
    if len(split_bin) != 4:
        return "Error - Invalid IP"
    for part in split_bin:
        decimal += str(binary_to_decimal(part)) + "."
    return decimal[:-1]

def ip_convert(ip):
    if is_valid_ip(ip):
        return ip_to_binary(ip)
    elif is_valid_binary(ip):
        return binary_to_ip(ip)
    else:
        return "Error - Invalid IP"