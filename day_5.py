from utils import read_data
import copy


def get_stacks(data: list[str]) -> list[list[str]]:
    stacks = [ [] for i in range(9) ]
    for row in data[:8]:
        for index, i in enumerate(range(1, 35, 4)):
            if row[i] != ' ':
                stacks[index].append(row[i])
    
    for i in range(len(stacks)):
        stacks[i].reverse()

    return stacks


def part_1(data: list[str], stacks: list[list[str]]) -> str:
    for instruction in data[10:]:
        instruction = instruction.split(' ')
        
        number_of_crate = int(instruction[1])
        start_stack = int(instruction[3])
        end_stack = int(instruction[5])

        for i in range(number_of_crate):
            stacks[end_stack - 1].append(stacks[start_stack - 1].pop())

    result = ''
    for stack in stacks:
        result += stack[-1]

    return result


def part_2(data: list[str], stacks: list[list[str]]) -> str:
    for instruction in data[10:]:
        instruction = instruction.split(' ')
        
        number_of_crate = int(instruction[1])
        start_stack = int(instruction[3])
        end_stack = int(instruction[5])

        stacks[end_stack - 1] += stacks[start_stack - 1][-number_of_crate:]
        stacks[start_stack - 1] = stacks[start_stack - 1][:-number_of_crate]

    result = ''
    for stack in stacks:
        result += stack[-1]

    return result


if __name__ == '__main__':
    data = read_data('data/input_day_5.txt')
    stacks = get_stacks(data)

    print(part_1(data, copy.deepcopy(stacks)))
    print('--------')
    print(part_2(data, stacks))
