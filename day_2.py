from utils import read_data


def part_1(data: list[str]) -> int:
    point = 0
    for round in data:
        opponent = round.split(' ')[0]
        player = round.split(' ')[1]

        if player == 'X':
            point += 1
            if opponent == 'B':
                point += 0
            elif opponent == 'A':
                point += 3
            else:
                point += 6

        if player == 'Y':
            point += 2
            if opponent == 'B':
                point += 3
            elif opponent == 'A':
                point += 6
            else:
                point += 0

        if player == 'Z':
            point += 3
            if opponent == 'B':
                point += 6
            elif opponent == 'A':
                point += 0
            else:
                point += 3
    
    return point


def part_2(data: list[str]) -> int:
    point = 0
    for round in data:
        opponent = round.split(' ')[0]
        result = round.split(' ')[1]

        if result == 'Z':
            point += 6

            if opponent == 'A':
                point += 2
            elif opponent == 'B':
                point += 3
            else:
                point += 1
        
        if result == 'X':
            if opponent == 'A':
                point += 3
            elif opponent == 'B':
                point += 1
            else:
                point += 2
        
        if result == 'Y':
            point += 3

            if opponent == 'A':
                point += 1
            elif opponent == 'B':
                point += 2
            else:
                point += 3
    
    return point


if __name__ == '__main__':
    data = read_data('data/input_day_2.txt')

    print(part_1(data))
    print('---------------')
    print(part_2(data))
