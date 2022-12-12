from utils import read_data


def return_signal_strength_for_specific_cycle(cycle: int, x: int) -> int:
    if cycle in [20, 60, 100, 140, 180, 220]:
        return cycle * x
    
    return 0


def part_1(data: list[str]) -> int:
    result = 0
    cycle = 0
    x = 1
    for instruction in data:
        if instruction.split(' ')[0] == 'addx':
            for _ in range(2):
                cycle += 1
                result += return_signal_strength_for_specific_cycle(cycle, x)
            x += int(instruction.split(' ')[1])
        else:
            cycle += 1
            result += return_signal_strength_for_specific_cycle(cycle, x)
    
    return result


def part_2(data: list[str]) -> None:
    x = 1
    cycle = 0
    crt = ''
    for instruction in data:
        if instruction.split(' ')[0] == 'addx':
            for _ in range(2):
                cycle += 1

                print('-----------')
                print(f'{cycle%40} in {[x-1, x, x+1]}')

                if ((cycle % 40) - 1) in [x-1, x, x+1]:
                    print('#')
                    crt += '#'
                else:
                    print('.')
                    crt += '.'

                if cycle in [40, 80, 120, 160, 200, 240]:
                    crt += '\n'

            x += int(instruction.split(' ')[1])
        else:
            cycle += 1

            print('-----------')
            print(f'{cycle%40} in {[x-1, x, x+1]}')

            if ((cycle % 40) - 1) in [x-1, x, x+1]:
                    print('#')
                    crt += '#'
            else:
                print('.')
                crt += '.'

            if cycle in [40, 80, 120, 160, 200, 240]:
                crt += '\n'
            
            
    print(crt)


if __name__ == '__main__':
    data = read_data('data/input_day_10.txt')
    
    print(part_1(data))
    print('--------')
    part_2(data)



# if cycle in [40, 80, 120, 160, 200, 240]:
                #     crt += '\n'
                #     continue

                # if (cycle%40) in [x - 1, x, x + 1]:
                #     crt += '#'
                # else:
                #     crt += '.'