def regionNum(grid):
    n_len = len(grid) * 3
    n_grid = [[0] * n_len for i in range(n_len)]
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] == '/':
                n_grid[i * 3 + 2][j * 3], n_grid[i * 3 + 1][j * 3 + 1], n_grid[i * 3][j * 3 + 2] = 1, 1, 1
            if grid[i][j] == '\\':
                n_grid[i * 3][j * 3], n_grid[i * 3 + 1][j * 3 + 1], n_grid[i * 3 + 2][j * 3 + 2] = 1, 1, 1

    count = 0
    for i in range(n_len):
        for j in range(n_len):
            if n_grid[i][j] == 0:
                count += 1
                dfs(n_grid, i, j)
    return count

def dfs(n_grid, i, j):
    if i >= 0 and j >= 0 and i < len(n_grid) and j < len(n_grid) and n_grid[i][j] == 0:
        n_grid[i][j] = 1
        dfs(n_grid, i - 1, j)
        dfs(n_grid, i + 1, j)
        dfs(n_grid, i, j - 1)
        dfs(n_grid, i, j + 1)


leftbracket = input()
lines = []
line = input()
while line != ']':
    lines.append(eval(line.lstrip().replace(',','')))
    line = input()
print(regionNum(lines))
