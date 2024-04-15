# Чтение судоку из файла
def readFile():
    with open('input.txt') as file:
        rows = []
        for line in file:
            rows.append([int(x) for x in line.split()])
        return rows

# Сохранение судоку в файл
def saveFile(puzzle):
    with open('output.txt', 'w') as f:
        for row in puzzle:
            f.write(' '.join(str(x) for x in row) + '\n')

# Основная функция для поиска решения
def solveSudoku(puzzle):
    row, column = findEmptyCell(puzzle)

    if row is None and column is None:
        return True

    for num in range(1, 10):
        if checkValidPuzzle(puzzle, row, column, num):
            puzzle[row][column] = num
            if solveSudoku(puzzle):
                return True
            puzzle[row][column] = 0

    return False

# Поиск пустых ячеек (0)
def findEmptyCell(puzzle):
    for i in range(9):
        for j in range(9):
            if puzzle[i][j] == 0:
                return i, j

    return None, None

# Проверка ряда, колонки и поля 3x3 на существование числа в них
def checkValidPuzzle(puzzle, row, column, number):
    # Определение стартовых позиций для проверки полей 3х3
    start_pos_row = row - row % 3
    start_pos_column = column - column % 3

    # Проверка ряда
    if number in [puzzle[row][i] for i in range(9)]:
        return False

    # Проверка колонки
    if number in [puzzle[i][column] for i in range(9)]:
        return False

    # Проверка блока 3x3
    if number in [puzzle[start_pos_row + i][start_pos_column + j] for i in range(3) for j in range(3)]:
        return False

    return True

if __name__ == "__main__":
    # Входная таблица судоку
    puzzle = readFile()

    if solveSudoku(puzzle):
        saveFile(puzzle)
    else:
        print("Impossible")