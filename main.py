from assembler.lexer import tokenize_line
from assembler.parser import parse_tokens

with open("input/program1.mas", "r") as file:
    lines = file.readlines()

for line in lines:

    line = line.strip()

    if not line:
        continue

    tokens = tokenize_line(line)

    parsed = parse_tokens(tokens)

    print(parsed)