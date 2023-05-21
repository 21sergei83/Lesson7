def print_operation_table(operation, num_rows=6, num_columns=6):
    # печатаем заголовок таблицы
    print('  |', end='')
    for j in range(1, num_columns + 1):
        print(f' {j} |', end='')
    print()
    print('--+' + '---+' * num_columns)

    # печатаем строки таблицы
    for i in range(1, num_rows + 1):
        print(f'{i} |', end='')
        for j in range(1, num_columns + 1):
            result = operation(i, j)
            print(f' {result} |', end='')
        print()
        print('--+' + '---+' * num_columns)
