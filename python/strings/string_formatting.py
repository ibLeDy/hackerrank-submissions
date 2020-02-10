def print_formatted(number):
    binary_number = str(bin(number).split('b')[-1])

    for i in range(1, number + 1):
        decimal = i
        octal = oct(i).split('o')[-1]
        hexadecimal = hex(i).split('x')[-1]
        binary = bin(i).split('b')[-1]

        print("{} {} {} {}".format(str(decimal).rjust(len(binary_number)),
                                   str(octal).rjust(len(binary_number)),
                                   str(hexadecimal).upper().rjust(len(binary_number)),
                                   str(binary).rjust(len(binary_number))))
