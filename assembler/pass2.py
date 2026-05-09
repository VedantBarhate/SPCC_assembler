from assembler.opcode_table import OPCODES

def run_pass2(parsed_statements, symbol_table):
    machine_code = []
    for statement in parsed_statements:
        # Skip VAR declarations
        if statement["type"] == "VAR":
            continue
        opcode_name = statement["opcode"]
        
        # Get opcode number
        opcode = OPCODES[opcode_name]

        # DISPLAY() has no operand
        if opcode_name == "DISPLAY":

            instruction = opcode
        else:
            operand = statement["operand"]
            # Resolve symbol address
            address = symbol_table.get_address(operand)
            instruction = f"{opcode} {address}"

        machine_code.append(instruction)

    return machine_code