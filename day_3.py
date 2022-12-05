from utils import read_data


def part_1(data: list[str]) -> int:
    priority = 0
    for rucksacks in data:
        compartment_1 = rucksacks[:(len(rucksacks)//2)]
        compartment_2 = rucksacks[(len(rucksacks)//2):]
        
        for c in compartment_1:
            index = compartment_2.find(c)
            if index != -1:
                ascii_number = ord(c)

                if 97 <= ascii_number <= 122:
                    priority += ascii_number - 96
                elif 65 <= ascii_number <= 90:
                    priority += ascii_number - 38
                
                break

    return priority


def part_2(data: list[str]) -> int:
    # Group of three elv
    groups = []
    for i in range(0, len(data), 3):
        groups.append(data[i:i+3])

    priority = 0
    for group in groups:
        rucksacks_1 = group[0]
        rucksacks_2 = group[1]
        rucksacks_3 = group[2]

        for c in rucksacks_1:
            index = rucksacks_2.find(c)
            if index != -1:
                index = rucksacks_3.find(c)
                if index != -1:
                    ascii_number = ord(c)

                    if 97 <= ascii_number <= 122:
                        priority += ascii_number - 96
                    elif 65 <= ascii_number <= 90:
                        priority += ascii_number - 38
                    
                    break
    
    return priority


if __name__ == '__main__':
    data = read_data('data/input_day_3.txt')

    print(part_1(data))
    print('---------------')
    print(part_2(data))
