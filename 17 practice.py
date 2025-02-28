def add_user(name: str, atten: int, filename: str) -> None:

    try:
        with open(filename, 'r+') as file:
            lines = file.readlines()
            users = [line.strip().split(',')[0] for line in lines]
            if name not in users:
                file.seek(0)
                file.write(f"{name},{atten}\n" + ''.join(lines))
    except FileNotFoundError:
        with open(filename, 'w') as file:
            file.write(f"{name},{atten}\n")


def pop_user(name: str, filename: str) -> tuple:

    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            users = [line.strip().split(',')[0] for line in lines]
            if name in users:
                index = users.index(name)
                removed_user = lines.pop(index).strip().split(',')
                with open(filename, 'w') as file:
                    file.write(''.join(lines))
                return tuple(removed_user)
            else:
                return ("name", 0)
    except FileNotFoundError:
        return ("name", 0)