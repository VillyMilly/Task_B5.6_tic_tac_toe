def greetings():
    print(f'Игра "Крестики-Нолики" приветствует вас!\n'
          f'\n'
          f'Вводится две координаты через пробел:\n'
          f'- номер строки\n'
          f'- номер столбца\n')
    return input('Игрок "Х", введите своё имя: '), input('Игрок "0", введите своё имя: ')

def output_table():
    print(' | 0 | 1 | 2 |')
    print('--------------')
    for i, value in enumerate(field):
        print(f"{i}| {' | '.join(value)} |")
        print('--------------')

def data_input():
    while True:
        coordinates = input('Введите 2 координаты через пробел: ').split()
        if len(coordinates) != 2:
            print('Необходимо ввести две цифры!')
            continue
        if not coordinates[0].isdigit() or not coordinates[1].isdigit():
            print('Координатами могут быть только целые положительные числа!')
            continue

        x, y = map(int, coordinates)

        if x > 2 or y > 2:
            print('Координаты должны находится в диапазоне от 0 до 2 включительно')
            continue
        if field[x][y] != ' ':
            print('Увы, ячейка уже занята:( Выберите другую')
            continue

        return x, y

def win():
    winning_combination = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                           ((0, 0), (1, 0), (2, 0)), ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)),
                           ((0, 0), (1, 1), (2, 2)), ((0, 2), (1, 1), (2, 0)))
    for i in winning_combination:
        symbols = []
        for j in i:
            symbols.append(field[j[0]][j[1]])
        if symbols == ["X", "X", "X"]:
            print(f"Выиграл(а) {player1}! Поздравляем!")
            return True
        if symbols == ["0", "0", "0"]:
            print(f"Выиграл(а) {player2}! Поздравляем!")
            return True

player1, player2 = greetings()
field = [[' ']*3 for i in range(3)]
output_table()
count = 0

while True:
    if count % 2 == 0:
        player_number = 'X'
        print(f'{player1}, ваш ход!')
    else:
        player_number = '0'
        print(f'{player2}, ваш ход!')
    x, y = data_input()
    field[x][y] = player_number
    output_table()
    count += 1
    if count > 4:
        if win():
            break
    if count > 8:
        print('Ничья! Партия завершена!')
        break