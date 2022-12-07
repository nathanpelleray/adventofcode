from utils import read_data


class Node:
    def __init__(self, name: str, parent: 'Node' = None, value: int = 0) -> None:
        self.name = name
        self.value = value
        self.parent = parent
        self.children = []

    def insert_node(self, name: str, value: int = 0) -> 'Node':
        new_node = Node(name, self, value)
        self.children.append(new_node)
        return new_node

    def __str__(self) -> None:
        result = f'{self.name}[{self.value}]\n'
        for child in self.children:
            result += f'{self.name} - {child.name}[{child.value}]\n'
        
        return result


def create_tree(data: list[str]) -> Node:
    tree = Node('/')
    current_node = tree
    for command in data[1:]:
        command = command.split(' ')
        if command[0] == '$':
            if command[1] == 'ls':
                continue
            if command[1] == 'cd':
                if command[2] == '..':
                    current_node = current_node.parent
                else:
                    for child in current_node.children:
                        if child.name == command[2]:
                            current_node = child
        elif command[0] == 'dir':
            current_node.insert_node(command[1])
        else:
            current_node.insert_node(command[1], int(command[0]))
    
    return tree


def calculate_size_of_repertory(tree: Node) -> None:
    for child in tree.children:
        calculate_size_of_repertory(child)
    
    for child in tree.children:
        tree.value += child.value


def part_1(tree: Node) -> int:
    if len(tree.children) == 0:
            return 0

    result = 0
    if tree.value <= 100000:
        result += tree.value

    for child in tree.children:
        result += part_1(child)

    return result


def find_potential_repertories(tree: Node, space: int) -> int:
    if len(tree.children) == 0:
            return []
    
    potential_repertories = []
    if tree.value >= space:
        potential_repertories.append(tree)

    for child in tree.children:
        potential_repertories += find_potential_repertories(child, space)
    
    return potential_repertories


def part_2(tree: Node) -> int:
    potential_repertories = find_potential_repertories(tree, 30000000 - (70000000 - tree.value))
    
    smallest_size = 70000000
    for repertory in potential_repertories:
        if repertory.value < smallest_size:
            smallest_size = repertory.value

    return smallest_size

        

if __name__ == '__main__':
    data = read_data('data/input_day_7.txt')
    tree = create_tree(data)
    calculate_size_of_repertory(tree)
    
    print(part_1(tree))
    print('--------')
    print(part_2(tree))
