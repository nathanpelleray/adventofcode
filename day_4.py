from utils import read_data


def part_1(data: list[str]) -> int:
    number_fully_contain = 0
    for pair in data:
        range_1 = pair.split(',')[0]
        range_2 = pair.split(',')[1]

        range_1 = range_1.split('-')
        range_2 = range_2.split('-')

        # range 1 contain range 2
        if int(range_1[0]) <= int(range_2[0]) and int(range_2[1]) <= int(range_1[1]):
            number_fully_contain += 1
            continue

        # range 2 contain range 1
        if int(range_2[0]) <= int(range_1[0]) and int(range_1[1]) <= int(range_2[1]):
            number_fully_contain += 1
            continue

    return number_fully_contain


def part_2(data: list[str]) -> int:
    number_range_overlap = 0
    for pair in data:
        range_1 = pair.split(',')[0]
        range_2 = pair.split(',')[1]

        range_1 = range_1.split('-')
        range_2 = range_2.split('-')

        # range 1 overlap range 2
        if int(range_1[0]) <= int(range_2[0]) <= int(range_1[1]):
            number_range_overlap += 1
            continue
        if int(range_1[0]) <= int(range_2[1]) <= int(range_1[0]):
            number_range_overlap += 1
            continue

        # range 2 overlap range 1
        if int(range_2[0]) <= int(range_1[0]) <= int(range_2[1]):
            number_range_overlap += 1
            continue
        if int(range_2[0]) <= int(range_1[1]) <= int(range_2[0]):
            number_range_overlap += 1
            continue

    return number_range_overlap


if __name__ == '__main__':
    data = read_data('data/input_day_4.txt')

    print(part_1(data))
    print('--------')
    print(part_2(data))
