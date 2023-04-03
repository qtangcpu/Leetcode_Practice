# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


def traverse_matrix(matrix):

    rows, cols = len(matrix), len(matrix[0])

    # Initialize the matrix of point values and the optimal score matrix
    optimal_score = [[0 for j in range(cols)] for i in range(rows)]
    optimal_score[0][0] = matrix[0][0]  # Initialize first row

    for i in range(1, rows):
        optimal_score[i][0] = optimal_score[i-1][0] + matrix[i][0]  # Initialize first column

    for j in range(1, cols):
        optimal_score[0][j] = optimal_score[0][j-1] + matrix[0][j]

    # Compute the optimal score for each cell
    for i in range(1, rows):
        for j in range(1, cols):
            optimal_score[i][j] = max(optimal_score[i-1][j], optimal_score[i][j-1]) + matrix[i][j]

    path = []
    distance = rows + cols - 2

    a = rows-1
    b = cols-1
    while a != 0 or b != 0:
        if a >= 1 and b >= 1:
            if optimal_score[a-1][b] > optimal_score[a][b-1]:
                path.append("d")
                a -= 1
            else:
                path.append("r")
                b -= 1
        elif a==0:
            path.append("r")
            b -= 1
        elif b==0:
            path.append("d")
            a -= 1

    return [optimal_score[rows - 1][cols - 1], path]


def max_traverse(matrix):
    rows, cols = len(matrix), len(matrix[0])
    matrix1 = [[matrix[i][j] for j in range(cols//2 + 1)] for i in range(rows//2+1)]
    traverse1 = traverse_matrix(matrix1)
    point1 = traverse1[0]
    path1 = traverse1[1]
    matrix2 = [[matrix[i][cols//2-j] for j in range(cols // 2 + 1)] for i in range(rows // 2+1)]
    traverse2 = traverse_matrix(matrix2)
    point2 = traverse2[0]
    path2 = traverse2[1]
    for i in range(len(path2)):
        if path2[i] == "r":
            path2[i] = "l"
    matrix3 = [[matrix[rows//2-i][cols//2-j] for j in range(cols // 2 + 1)] for i in range(rows // 2+1)]
    traverse3 = traverse_matrix(matrix3)
    point3 = traverse3[0]
    path3 = traverse3[1]
    for i in range(len(path3)):
        if path3[i] == "r":
            path3[i] = "l"
        if path3[i] == "d":
            path3[i] = "u"
    matrix4 = [[matrix[rows // 2 - i][j] for j in range(cols // 2 + 1)] for i in range(rows // 2+1)]
    traverse4 = traverse_matrix(matrix4)
    point4 = traverse4[0]
    path4 = traverse4[1]
    for i in range(len(path4)):
        if path4[i] == "d":
            path4[i] = "u"

    max_point = max(point1, point2, point3, point4)
    if max_point == point1:
        return path1
    elif max_point == point2:
        return path2
    elif max_point == point3:
        return path3
    elif max_point == point4:
        return path4


input_string = input()
rows = input_string.split(";")
matrix = []
for row in rows:
    columns = row.split(",")
    matrix.append(columns)

matrix_integers = []
for row in matrix:
    row_integers = []
    for column in row:
        row_integers.append(int(column))
    matrix_integers.append(row_integers)

print(*max_traverse(matrix_integers), sep=",")