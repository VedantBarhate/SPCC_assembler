VALID_INSTRUCTIONS = [
    "LOAD",
    "STORE",
    "ADD",
    "SUB",
    "MULT",
    "DIV",
    "DISPLAY"
]


def is_valid_identifier(name):
    if not name:
        return False
    if not name[0].isalpha():
        return False
    return name.replace("_", "").isalnum()


def parse_tokens(tokens):

    if not tokens:
        raise Exception("Empty statement")

    # VAR DECLARATION
    if tokens[0] == "VAR":
        if len(tokens) != 4:
            raise Exception("Invalid VAR statement")
        if tokens[3] != ";":
            raise Exception("Missing semicolon")
        variable_name = tokens[1]
        variable_value = tokens[2]
        # Validate identifier
        if not is_valid_identifier(variable_name):
            raise Exception(f"Invalid variable name: {variable_name}")
        # Validate integer value
        if not variable_value.isdigit():
            raise Exception(f"Invalid numeric value: {variable_value}")
        return {
            "type": "VAR",
            "name": variable_name,
            "value": int(variable_value)
        }

    # DISPLAY()
    elif tokens[0] == "DISPLAY":
        if tokens != ['DISPLAY', '(', ')', ';']:
            raise Exception("Invalid DISPLAY syntax")
        return {
            "type": "INSTRUCTION",
            "opcode": "DISPLAY",
            "operand": None
        }

    # OTHER INSTRUCTIONS
    elif tokens[0] in VALID_INSTRUCTIONS:
        if len(tokens) != 5:
            raise Exception("Invalid instruction format")
        if tokens[1] != '(':
            raise Exception("Missing '('")
        if tokens[3] != ')':
            raise Exception("Missing ')'")
        if tokens[4] != ';':
            raise Exception("Missing semicolon")
        operand = tokens[2]
        # Validate operand name
        if not is_valid_identifier(operand):
            raise Exception(f"Invalid operand: {operand}")
        return {
            "type": "INSTRUCTION",
            "opcode": tokens[0],
            "operand": operand
        }

    # UNKNOWN INSTRUCTION
    else:
        raise Exception(f"Unknown instruction: {tokens[0]}")