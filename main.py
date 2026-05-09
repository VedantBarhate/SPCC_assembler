from assembler.lexer import tokenize_line
from assembler.parser import parse_tokens
from assembler.pass1 import run_pass1
from assembler.pass2 import run_pass2
from assembler.simulator import run_simulator

parsed_statements = []

# READ SOURCE PROGRAM
with open("input/program1.mas", "r") as file:
    lines = file.readlines()

# LEXER + PARSER
for line in lines:
    line = line.strip()
    if not line:
        continue

    tokens = tokenize_line(line)
    parsed = parse_tokens(tokens)
    parsed_statements.append(parsed)

# PASS 1
symbol_table = run_pass1(parsed_statements)

symbol_table.display()

# PASS 2
machine_code = run_pass2(parsed_statements, symbol_table)

print("\nMACHINE CODE")
print("-" * 30)

for instruction in machine_code:
    print(instruction)

# SIMULATOR
final_memory = run_simulator(machine_code, symbol_table)

print("\nFINAL MEMORY")
print("-" * 30)

for address, value in final_memory.items():
    print(f"{address} -> {value}")