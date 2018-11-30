import os
from collections import Counter


def gen_files(pat):
    for directory in os.walk(pat):
        for filename in directory[-1]:
            if filename.endswith('.py'):
                yield '{}/{}'.format(directory[0], filename)


def gen_lines(files):
    for file_path in files:
        with open(file_path) as f:
            for line in f.readlines():
                yield line


def gen_grep(lines, pattern):
    for line in lines:
        if line.startswith(pattern):
            yield line


if __name__ == '__main__':
    counter = Counter()
    for i in gen_grep(gen_lines(gen_files('..')), 'import '):
        counter[i.split()[1]] += 1

    for v, c in sorted(counter.items(), key=lambda x: x[1], reverse=True):
        print('      {} {}'.format(c, v))
