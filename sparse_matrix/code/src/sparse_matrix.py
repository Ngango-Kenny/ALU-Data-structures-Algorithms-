class SparseMatrix:
    def __init__(self, matrixFilePath=None, numberRows=None, numberCols=None):
        if matrixFilePath:
            self.load_from_file(matrixFilePath)
        elif numberRows and numberCols:
            self.numberRows = numberRows
            self.numberCols = numberCols
            self.data = {}

    def load_from_file(self, matrixFilePath):
        with open(matrixFilePath, 'r') as file:
            lines = file.readlines()
            self.numberRows = None
            self.numberCols = None
            self.data = {}
            for line in lines:
                line = line.strip()
                if line.startswith("rows"):
                    self.numberRows = int(line.split('=')[1])
                elif line.startswith("cols"):
                    self.numberCols = int(line.split('=')[1])
                else:
                    row, col, value = map(int, line[1:-1].split(','))
                    self.data[(row, col)] = value

            if self.numberRows is None or self.numberCols is None:
                raise ValueError("Matrix dimensions not found in the file.")

    def get_element(self, currentRow, currentCol):
        return self.data.get((currentRow, currentCol), 0)

    def set_element(self, currentRow, currentCol, value):
        self.data[(currentRow, currentCol)] = value

    def add(self, other):
        if self.numberRows != other.numberRows or self.numberCols != other.numberCols:
            raise ValueError("Matrices must have the same dimensions for addition.")
        result = SparseMatrix(numRows=self.numberRows, numCols=self.numberCols)
        for i in range(self.numberRows):
            for j in range(self.numberCols):
                result.set_element(i, j, self.get_element(i, j) + other.get_element(i, j))
        return result

    def subtract(self, other):
        if self.numberRows != other.numberRows or self.numberCols != other.numberCols:
            raise ValueError("Matrices must have the same dimensions for subtraction.")
        result = SparseMatrix(numberRows=self.numberRows, numberCols=self.numberCols)
        for i in range(self.numberRows):
            for j in range(self.numberCols):
                result.set_element(i, j, self.get_element(i, j) - other.get_element(i, j))
        return result

    def multiply(self, other):
        if self.numberCols != other.numberRows:
            raise ValueError("Number of columns in the first matrix must be equal to the number of rows in the second matrix for multiplication.")
        result = SparseMatrix(numberRows=self.numberRows, numberCols=other.numberCols)
        for i in range(self.numberRows):
            for j in range(other.numberCols):
                sum = 0
                for k in range(self.numberCols):
                    sum += self.get_element(i, k) * other.get_element(k, j)
                result.set_element(i, j, sum)
        return result

    def print_matrix(self):
        for row in range(self.numberRows):
            for col in range(self.numberCols):
                print(self.get_element(row, col), end='\t')
            print()

if __name__ == "__main__":
    matrix1 = SparseMatrix(matrixFilePath="sparse_matrix_input1.txt")
    matrix2 = SparseMatrix(matrixFilePath="sparse_matrix_input2.txt")

    # Addition
    try:
        result_addition = matrix1.add(matrix2)
        print("Addition Result:")
        result_addition.print_matrix()
    except:
        print("Error during addition")

    # Subtraction
    try:
        result_subtraction = matrix1.subtract(matrix2)
        print("\nSubtraction Result:")
        result_subtraction.print_matrix()
    except:
        print("Error during subtraction")

    # Multiplication
    try:
        result_multiplication = matrix1.multiply(matrix2)
        print("\nMultiplication Result:")
        result_multiplication.print_matrix()
    except:
        print("Error during multiplication")
