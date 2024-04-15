# Чтение из файла
def readFile():
    with open('input.txt') as file:
        cycles = int(file.readline().split()[0])
        rows = []
        for line in file:
            rows.append([int(x) for x in line.split()])
        return cycles, rows


# Запись и сохранение файла
def saveFile(puzzle):
    with open('output.txt', 'w') as f:
        for row in puzzle:
            f.write(' '.join(str(x) for x in row) + '\n')


# Проверка цикла
def check_rows(rows):
    new_rows = list(map(list, rows))
    for i in range(9):
        for j in range(9):
            neighbours = neighbours_count(rows, i, j)

            if rows[i][j] == 0:
                if neighbours == 3:
                    new_rows[i][j] = 1
            else:
                if neighbours != 2 and neighbours != 3:
                    new_rows[i][j] = 0

    return new_rows


# Подсчет количества живых соседей
def neighbours_count(rows, row, column):
    delta_rows = [-1, 0, 1]
    delta_cols = [-1, 0, 1]

    neighbours = 0

    for dr in delta_rows:
        for dc in delta_cols:
            if dr == dc == 0:
                continue
            r, c = (row + dr) % 9, (column + dc) % 9
            neighbours += rows[r][c]

    return neighbours


if __name__ == '__main__':
    cycles, rows = readFile()

    for _ in range(cycles - 1):
        rows = check_rows(rows)

    saveFile(rows)
