from utils import read_data


def part_1(data: list[str]) -> int:
    calories = 0
    max_calories = 0
    for i in data:
        if i == '':
            calories = 0
            continue

        calories += int(i)
        if calories > max_calories:
            max_calories = calories
    
    return max_calories


def part_2(data: list[str]) -> int:
    calories = 0
    list_elves = []
    for i in data:
        if i == '':
            list_elves.append(calories)
            calories = 0
            continue

        calories += int(i)

    list_elves.sort()
    list_elves = list_elves[-3:]

    calories = 0
    for i in list_elves:
        calories += i
    
    return calories


if __name__ == '__main__':
    data = read_data('data/input_day_1.txt')

    print(part_1(data))
    print('---------------')
    print(part_2(data))