def read_data(path: str) -> list[str]:
    with open(path, 'r') as f:
        file = f.read()

    return file.split('\n')
