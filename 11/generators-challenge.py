import os


def gen_files(pat):
    for directory in os.walk(pat):
        for filename in directory[-1]:
            if filename.endswith('.py'):
                yield '{}/{}'.format(directory[0], filename)


if __name__ == '__main__':
    for file in gen_files('..'):
        print(file)
