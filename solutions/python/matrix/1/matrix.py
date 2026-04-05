class Matrix:
    def __init__(self, matrix_string):
        if not matrix_string:
            raise ValueError("Empty")
            
        self.matrix_string = matrix_string
        self.matrix = [[int(num) for num in row.split(' ')] for row in self.matrix_string.strip().split('\n')]
        
        # for row in self.matrix_string.strip().split('\n'):
        #     numbers = [int(num) for num in row.split(' ')]
        #     # for num in row.split(' '):
        #     #     numbers.append(int(num))
        #     self.matrix.append(numbers)

    def row(self, index):
        return self.matrix[index - 1]

    def column(self, index):
        column = []
        for i in range(len(self.matrix)):
            column.append(self.matrix[i][index - 1])
        return column
            
