from assembler.lexer import tokenize_line
from assembler.parser import parse_tokens
from assembler.pass1 import run_pass1

parsed_statements = []

with open("input/program1.mas", "r") as file:
    lines = file.readlines()

for line in lines:

    line = line.strip()

    if not line:
        continue

    tokens = tokenize_line(line)

    parsed = parse_tokens(tokens)

    parsed_statements.append(parsed)

# PASS 1
symbol_table = run_pass1(parsed_statements)

# DISPLAY SYMBOL TABLE
symbol_table.display()