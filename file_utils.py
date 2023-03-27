

def file_open(path):
   with open(path, 'r') as f:
    file_list = [line.strip() for line in f]
    return file_list


def file_write(path, filename, file_list):
    with open(f'{path}{filename}', 'w') as f:
        for line in file_list:
            f.write(f"{line}\n")
