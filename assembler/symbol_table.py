class SymbolTable:
    def __init__(self):
        self.table = {}

    def add_symbol(self, name, address, value):
        if name in self.table:
            raise Exception(f"Duplicate symbol: {name}")

        self.table[name] = {
            "address": address,
            "value": value
        }

    def exists(self, name):
        return name in self.table

    def get_address(self, name):
        if name not in self.table:
            raise Exception(f"Undefined symbol: {name}")

        return self.table[name]["address"]

    def get_value(self, name):
        if name not in self.table:
            raise Exception(f"Undefined symbol: {name}")

        return self.table[name]["value"]

    def display(self):
        print("\nSYMBOL TABLE")
        print("-" * 30)

        for symbol, data in self.table.items():
            print(f"{symbol} -> Address: {data['address']}, Value: {data['value']}")