
class SpreadSheet:

    def __init__(self):
        self._cells = {}
        self._evaluating = set()  # Set to track cells currently being evaluated

    def set(self, cell: str, value: str) -> None:
        self._cells[cell] = value

    def get(self, cell: str) -> str:
        return self._cells.get(cell, '')

    def evaluate(self, cell: str) -> int | str:
        if cell in self._evaluating:
            return "#Circular"
        self._evaluating.add(cell)
        
        value = self.get(cell)
        if value.isdigit():
            result = int(value)
        elif value.startswith("'") and value.endswith("'"):
            result = value[1:-1]
        elif value.startswith("="):
            if value[1:].isdigit():
                result = int(value[1:])
            elif value.startswith("='") and value.endswith("'"):
                result = value[2:-1]
            else:
                # Evaluate reference to another cell
                reference = value[1:]
                if reference in self._cells:
                    result = self.evaluate(reference)
                else:
                    result = "#Error"
        else:
            result = "#Error"
        
        self._evaluating.remove(cell)
        return result

