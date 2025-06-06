def max_experience_with_path(levels):
    n = len(levels)
    dp = levels[-1][:]
    path = [[i] for i in range(len(levels[-1]))]

    for i in range(n - 2, -1, -1):
        new_dp = []
        new_path = []
        for j in range(len(levels[i])):
            if dp[j] >= dp[j + 1]:
                best_next = dp[j]
                best_path = path[j]
            else:
                best_next = dp[j + 1]
                best_path = path[j + 1]
            new_dp.append(levels[i][j] + best_next)
            new_path.append([j] + best_path)
        dp = new_dp
        path = new_path

    return dp[0], path[0]

def read_input(filename):
    with open(filename, 'r') as f:
        L = int(f.readline())
        levels = []
        for _ in range(L):
            levels.append(list(map(int, f.readline().split())))
    return levels

def write_output(filename, result, path_values):
    with open(filename, 'w') as f:
        f.write(str(result) + '\n')
        f.write(' '.join(map(str, path_values)) + '\n')

if __name__ == "__main__":
    levels = read_input('input.txt')
    result, path = max_experience_with_path(levels)
    path_values = [levels[i][j] for i, j in enumerate(path)]
    write_output('output.txt', result, path_values)
    print("Максимальний досвід:", result)
    print("Індекси:", path)
    print("Шлях:", path_values)
