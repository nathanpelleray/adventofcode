from utils import read_data


def part_1(data: str) -> int:
    fist_marker_index = 0
    for i in range(3,len(data)):
        if len(set(data[i-3:i+1])) == 4:
            fist_marker_index = i + 1
            break
    
    return fist_marker_index


def part_2(data: str) -> int:
    fist_marker_index = 0
    for i in range(13,len(data)):
        if len(set(data[i-13:i+1])) == 14:
            fist_marker_index = i + 1
            break
    
    return fist_marker_index


if __name__ == '__main__':
    data = read_data('data/input_day_6.txt')[0]

    print(part_1(data))
    print('--------')
    print(part_2(data))