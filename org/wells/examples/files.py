def create_file(filename):
    file = open(filename, 'w')

    file.write('Hello World!\n')
    file.write('This is our new text file.\n')
    file.write('and this is another line.\n')
    file.write('Why? Because we can.\n')
    file.close()


def read_file1(filename):
    file = open(filename, 'r')
    print(file.read())
    file.close()


def read_file2(filename):
    file = open(filename, 'r')
    print(file.read(5))
    file.close()


def read_file3(filename):
    file = open(filename, 'r')
    print(file.readline())
    print(file.readline())
    file.close()


def read_file4(filename):
    file = open(filename, 'r')
    print(file.readlines())
    file.close()


def read_file5(filename):
    with open(filename, 'r') as file:
        for line in file:
            print(line)


def file_test():
    filename = 'test.md'
    create_file(filename)

    # read_file1(filename)
    # read_file2(filename)
    read_file5(filename)


file_test()
