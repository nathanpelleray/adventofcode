from utils import read_data


def part_1(data: list[str]) -> int:
    visible_trees = 0
    for y in range(len(data)):
        for x in range(len(data[y])):
            # Top edge
            if y == 0:
                visible_trees += 1
                continue
            # Bottom edge
            elif y == len(data) - 1:
                visible_trees += 1
                continue
            # Left edge
            elif x == 0:
                visible_trees += 1
                continue
            # Right edge
            elif x == len(data[y]) - 1:
                visible_trees += 1
                continue

            top = bottom = left = right = True
            # Top
            for i in range(y - 1, -1, -1):
                if int(data[i][x]) >= int(data[y][x]):
                    top = False
                    break
            if top:
                visible_trees += 1
                continue

            # Bot
            for i in range(y + 1, len(data)):
                if int(data[i][x]) >= int(data[y][x]):
                    bottom = False
                    break
            if bottom:
                visible_trees += 1
                continue

            # left
            for i in range(x - 1, -1, -1):
                if int(data[y][i]) >= int(data[y][x]):
                    left = False
                    break
            if left:
                visible_trees += 1
                continue

            # right
            for i in range(x + 1, len(data[y])):
                if int(data[y][i]) >= int(data[y][x]):
                    right = False
                    break
            if right:
                visible_trees += 1
                continue

    return visible_trees


def part_2(data: list[str]) -> int:
    highest_scenic_score = 0
    for y in range(len(data)):
        for x in range(len(data[y])):
            # Top
            top_count = 0
            for i in range(y - 1, -1, -1):
                top_count += 1
                if int(data[i][x]) >= int(data[y][x]):
                    break

            # Bottom
            bottom_count = 0
            for i in range(y + 1, len(data)):
                bottom_count += 1
                if int(data[i][x]) >= int(data[y][x]):
                    break
            
            # Left
            left_count = 0
            for i in range(x - 1, -1, -1):
                left_count += 1
                if int(data[y][i]) >= int(data[y][x]):
                    break

            # Right
            right_count = 0
            for i in range(x + 1, len(data[y])):
                right_count += 1
                if int(data[y][i]) >= int(data[y][x]):
                    break
            
            tree_score = top_count * bottom_count * left_count * right_count
            if highest_scenic_score < tree_score:
                highest_scenic_score = tree_score
    
    return highest_scenic_score


if __name__ == '__main__':
    data = read_data('data/input_day_8.txt')

    print(part_1(data))
    print('--------')
    print(part_2(data))
    