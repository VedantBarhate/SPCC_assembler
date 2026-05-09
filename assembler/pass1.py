from assembler.symbol_table import SymbolTable


def run_pass1(parsed_statements):
    symbol_table = SymbolTable()
    current_address = 100

    for statement in parsed_statements:
        if statement["type"] == "VAR":
            variable_name = statement["name"]
            variable_value = statement["value"]

            symbol_table.add_symbol(
                variable_name,
                current_address,
                variable_value
            )

            current_address += 1

    return symbol_table