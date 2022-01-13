row = int(input('Enter the row(s): '))
semi_matrix = [[1 for i in range(row)] for j in range(row)]
for i in range(row):
    for j in range(1, i):
        semi_matrix[i][j] = semi_matrix[i - 1][j - 1] + semi_matrix[i - 1][j]
for i in range(row):
    for j in range(i + 1):
        print(semi_matrix[i][j], end=' ')
    print('')
