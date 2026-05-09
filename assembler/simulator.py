def run_simulator(machine_code, symbol_table):
    print("\nSIMULATOR OUTPUT")
    print("-" * 30)

    # ACC register
    acc = 0

    # Build memory from symbol table
    memory = {}

    for symbol, data in symbol_table.table.items():
        address = data["address"]
        value = data["value"]

        memory[address] = value

    # Execute instructions
    for instruction in machine_code:
        parts = instruction.split()
        opcode = parts[0]

        # DISPLAY
        if opcode == "07":
            print(f"OUTPUT: {acc}")
            continue

        # Instructions with operand
        address = int(parts[1])

        # LOAD
        if opcode == "01":
            acc = memory[address]
            print(f"LOAD -> ACC = {acc}")

        # STORE
        elif opcode == "02":
            memory[address] = acc
            print(f"STORE -> MEMORY[{address}] = {acc}")

        # ADD
        elif opcode == "03":
            acc += memory[address]
            print(f"ADD -> ACC = {acc}")

        # SUB
        elif opcode == "04":
            acc -= memory[address]
            print(f"SUB -> ACC = {acc}")

        # MULT
        elif opcode == "05":
            acc *= memory[address]
            print(f"MULT -> ACC = {acc}")

        # DIV
        elif opcode == "06":
            if memory[address] == 0:
                raise Exception("Division by zero")
            acc //= memory[address]
            print(f"DIV -> ACC = {acc}")

    return memory