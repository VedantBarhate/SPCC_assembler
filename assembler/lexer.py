DELIMITERS = ['(', ')', ';']


def tokenize_line(line):
    tokens = []
    current = ""

    for char in line:
        if char in [' ', '\n', '\t']:
            if current:
                tokens.append(current)
                current = ""
        elif char in DELIMITERS:
            if current:
                tokens.append(current)
                current = ""
            tokens.append(char)
        else:
            current += char

    if current:
        tokens.append(current)

    return tokens