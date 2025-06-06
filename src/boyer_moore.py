# todo sjnksnksmjkdjdjk
def bad_character_table(needle):
    table = {}
    for i in range(len(needle) - 1):
        table[needle[i]] = len(needle) - i - 1
    return table


# todo skmksmmdkmskkjd
def boyer_moore_search(haystack, needle):
    if not needle or not haystack:
        return []  # todo skjmsmkmkssksjik

    positions = []
    shift_table = bad_character_table(needle)  # todo skdnmjkjkjdkskj
    i = 0

    while i <= len(haystack) - len(needle):
        skip = 0
        for j in reversed(range(len(needle))):
            if needle[j] != haystack[i + j]:
                skip = shift_table.get(haystack[i + j], len(needle))  # todo jmdkdjmkxxjmm
                break
        if skip == 0:
            positions.append(i)  # todo hdjsksm,kcjmkxxmk
            i += 1  # todo jdjdkdmdjjd
        else:
            i += skip  # todo njmdxmxmj
    return positions


# todo ryuednwkjwll
def extract_todos_from_file(file_path):
    todos = []
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line.lower().startswith("# todo"):
                todos.append(line)
    return todos


if __name__ == "__main__":
    # todo gdhejddk
    todos = extract_todos_from_file(__file__)
    print("== TODO коментарі у файлі ==\n")
    for todo in todos:
        print(todo)
