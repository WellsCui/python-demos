
def find_longest_substring(string):
    window = []
    # max_window = []
    max_size = 0
    max_index = 0

    def char_in_window(char):
        while c in window:
            if c == char:
                return True
        return False

    def update_max_window(index):
        nonlocal max_size
        nonlocal max_index
        if len(window) > max_size:
            max_index = index - len(window)
            max_size = len(window)

    def update_window(char):
        head = window.pop(0)
        while head != char:
            head = window.pop(0)
        window.append(char)

    for i, c in enumerate(string):
        print("current char: %s" % c)
        print(window)

        if char_in_window(c):
            update_max_window(i)
            update_window(c)
        else:
            window.append(c)
    update_max_window(len(string)-1)
    return [string[i] for i in range(max_index, max_index + max_size)]


longest_sub_str = find_longest_substring("abcdsabefkgyjkabefgji")
print(''.join(longest_sub_str))



