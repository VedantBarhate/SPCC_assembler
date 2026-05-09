from assembler.lexer import tokenize_line

with open("input/program1.mas", "r") as file:
    lines = file.readlines()

for line in lines:
    line = line.strip()

    if line:
        tokens = tokenize_line(line)

        print(f"LINE: {line}")
        print(f"TOKENS: {tokens}")
        print()