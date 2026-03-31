DIGITS = {
    (" _ ", "| |", "|_|", "   "): "0",
    ("   ", "  |", "  |", "   "): "1",
    (" _ ", " _|", "|_ ", "   "): "2",
    (" _ ", " _|", " _|", "   "): "3",
    ("   ", "|_|", "  |", "   "): "4",
    (" _ ", "|_ ", " _|", "   "): "5",
    (" _ ", "|_ ", "|_|", "   "): "6",
    (" _ ", "  |", "  |", "   "): "7",
    (" _ ", "|_|", "|_|", "   "): "8",
    (" _ ", "|_|", " _|", "   "): "9",
}

def convert(input_grid):
    if isinstance(input_grid, list):
        lines = input_grid
    else:
        lines = input_grid.split("\n")

    if len(lines) % 4 != 0:
        raise ValueError("Number of input lines is not a multiple of four")

    for line in lines:
        if len(line) % 3 != 0:
            raise ValueError("Number of input columns is not a multiple of three")

    results = []

    for row_start in range(0, len(lines), 4):
        row_lines = lines[row_start:row_start + 4]
        num_digits = len(row_lines[0]) // 3
        row_result= ""

        for col in range(num_digits):
            start = col * 3
            cell = tuple(line[start:start + 3] for line in row_lines)
            row_result += DIGITS.get(cell, "?")

        results.append(row_result)

    return ",".join(results)

            
            

        


